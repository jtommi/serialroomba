from __future__ import annotations

from .state import StateEnum, State
from .controller import Controller


class Mode(StateEnum):
    OFF = State("Off", None, 0)
    FULL = State("Full", 132, 3)
    PASSIVE = State("Passive", 128, 1)
    SAFE = State("Safe", 131, 2)


class ModeController(Controller):
    @property
    def current_mode(self) -> Mode:
        ...  # TODO Read sensor value

    @current_mode.setter
    def current_mode(self, mode: Mode) -> None:
        self.serial_controller.send_command(mode.command)
