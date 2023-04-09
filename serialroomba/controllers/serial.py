from __future__ import annotations

from typing import TYPE_CHECKING

from serial import EIGHTBITS, PARITY_NONE, STOPBITS_ONE, Serial, SerialException

from ..exceptions import RoombaConnectionError

if TYPE_CHECKING:
    from serialroomba.controllers.sensors import SensorPacket


class ControlCodes:
    SENSOR = 142


class SerialController:
    def __init__(self, port: str, baud_rate: int, time_out_s: float) -> None:
        self._port = port
        self._baud_rate = baud_rate
        self._time_out_s = time_out_s

        self.connect_serial()

    def connect_serial(self) -> None:
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

    def send_command(self, command: int) -> None:
        if not isinstance(command, int):
            raise TypeError("Invalid command type")

        self.connection.write(bytes([command]))

    def send_command_with_data_bytes(self, command: int, data_bytes: bytes):
        self.send_command(command)
        self.connection.write(data_bytes)

    def send_sensor_request(self, sensor_packet: SensorPacket) -> bytes:
        self.send_command(ControlCodes.SENSOR)
        self.send_command(sensor_packet.packet_id)
        return self.connection.read(sensor_packet.number_of_bytes)
