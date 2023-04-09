from __future__ import annotations

from enum import Enum
from dataclasses import dataclass
from struct import Struct
from typing import TYPE_CHECKING, List

from serial import EIGHTBITS, PARITY_NONE, STOPBITS_ONE, Serial, SerialException

from ..exceptions import RoombaConnectionError

if TYPE_CHECKING:
    from serialroomba.controllers.sensors import SensorPacket


class ControlCodes:
    SENSOR = 142


@dataclass
class _DataType:
    struct_format: str
    number_of_bytes: int


class DataTypes(Enum):
    UNSIGNED_BYTE = _DataType("B", 1)
    SIGNED_BYTE = _DataType("b", 1)
    UNSIGNED_TWO_BYTES = _DataType("H", 2)
    SIGNED_TWO_BYTES = _DataType("h", 2)
    BOOL = _DataType("?", 1)

    @property
    def struct_format(self):
        return self.value.struct_format

    @property
    def number_of_bytes(self):
        return self.value.number_of_bytes


class SerialController:
    def __init__(self, port: str, baud_rate: int, time_out_s: float) -> None:
        self._port = port
        self._baud_rate = baud_rate
        self._time_out_s = time_out_s

        self._connect_serial()

    def _connect_serial(self) -> None:
        try:
            self.connection = Serial(
                self._port,
                baudrate=self._baud_rate,
                timeout=self._time_out_s,
                bytesize=EIGHTBITS,
                parity=PARITY_NONE,
                stopbits=STOPBITS_ONE,
                xonxoff=False,  # Flow control
            )
        except SerialException as exception:
            raise RoombaConnectionError(repr(exception)) from exception

        if not self.connection.is_open:
            raise RoombaConnectionError("Could not open the serial port")

    @staticmethod
    def _pack_data(command: int, data_bytes: List[int] = []):
        number_of_data_bytes = len(data_bytes)
        number_of_bytes = number_of_data_bytes + 1
        return Struct("B" * number_of_bytes).pack(command, *data_bytes)

    def send_command(self, command: int, data_bytes: int | List[int] = []):
        if isinstance(data_bytes, int):
            data_bytes = [data_bytes]

        command_and_data_bytes = self._pack_data(command, data_bytes)
        self.connection.write(command_and_data_bytes)

    def _send_sensor_request(self, packet_id: int, number_of_bytes: int) -> bytes:
        self.send_command(ControlCodes.SENSOR, packet_id)
        return self.connection.read(number_of_bytes)

    def get_sensor_data(self, sensor_packet: SensorPacket) -> bool | int:
        result = self._send_sensor_request(
            sensor_packet.packet_id, sensor_packet.data_type.number_of_bytes
        )
        return Struct(sensor_packet.data_type.struct_format).unpack(result)[0]
