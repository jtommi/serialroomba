from __future__ import annotations

from serialroomba.controllers.models.sensor import Sensor

from .controller import Controller
from .models.state import State, StateEnum
from .serial import DataTypes


class Mode(StateEnum):
    OFF = State("Off", None, 0)
    FULL = State("Full", 132, 3)
    PASSIVE = State("Passive", 128, 1)
    SAFE = State("Safe", 131, 2)


MODE_SENSOR = Sensor("Mode", 35, DataTypes.UNSIGNED_BYTE)


class ModeController(Controller):
    @property
    def current_mode(self) -> StateEnum:
        state_id = self.get_sensor_data(MODE_SENSOR)
        return Mode.from_state_id(state_id)

    @current_mode.setter
    def current_mode(self, mode: Mode) -> None:
        self.serial_controller.send_command(mode.command)
