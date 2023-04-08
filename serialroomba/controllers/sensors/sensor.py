from __future__ import annotations

from typing import TYPE_CHECKING

from ..controller import Controller

if TYPE_CHECKING:
    from serialroomba.controllers.serial import SerialController

    from .packet import SensorPacket


class Sensor(Controller):
    def __init__(self, serial_controller: SerialController) -> None:
        self.serial_controller = serial_controller

    @staticmethod
    def convert_bytes_to_sensor_value(bytes_result: bytes, packet: SensorPacket):
        return int.from_bytes(bytes_result, byteorder="big", signed=packet.signed)

    def get_sensor_data(self, packet) -> int:
        result = self.serial_controller.send_sensor_request(packet)

        return self.convert_bytes_to_sensor_value(result, packet)
