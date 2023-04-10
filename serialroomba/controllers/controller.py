from __future__ import annotations

from struct import Struct
from typing import TYPE_CHECKING

from .models.sensor import Sensor, SensorEnum

if TYPE_CHECKING:
    from serialroomba.controllers.serial import SerialController


class Controller:
    serial_controller: SerialController

    def __init__(self, serial_controller: SerialController) -> None:
        self.serial_controller = serial_controller

    def get_sensor_data(self, sensor: Sensor | SensorEnum) -> int | bool:
        returned_bytes = self.serial_controller.get_sensor_data(
            sensor.packet_id, sensor.data_type.number_of_bytes
        )
        return Struct(sensor.data_type.struct_format).unpack(returned_bytes)[0]

    @staticmethod
    def check_bit_is_set(data: int, bit_number: int) -> bool:
        """Checks if a specific bit is set in an integer

        Args:
            data (int): Data to check
            bit_number (int): Bit number 0-indexed

        Returns:
            bool: Whether the bit is set or not
        """
        bit = 0b1 << bit_number
        return bool(data & bit)
