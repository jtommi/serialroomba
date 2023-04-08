from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from serialroomba.controllers.serial import SerialController


class Controller:
    def __init__(self, serial_controller: SerialController) -> None:
        self.serial_controller = serial_controller
