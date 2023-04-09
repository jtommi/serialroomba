from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from serialroomba.controllers.serial import SerialController


class Controller:
    serial_controller: SerialController

    def __init__(self, serial_controller: SerialController) -> None:
        self.serial_controller = serial_controller

    def get_sensor_data(self, packet) -> int:
        return self.serial_controller.get_sensor_data(packet)
