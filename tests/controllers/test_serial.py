from unittest import TestCase
from unittest.mock import patch

from serialroomba.controllers.sensors.packet import SensorPacket
from serialroomba.controllers.serial import DataTypes, SerialController
from serialroomba.exceptions import RoombaConnectionError
from serialroomba.serialroomba import SerialRoomba


class TestSerialController(TestCase):
    @patch("serialroomba.controllers.serial.SerialController.connection")
    def test_serial_open_is_called(self, mock_connection):
        mock_connection.open.assert_not_called()
        _ = SerialRoomba("/dev/null")
        mock_connection.open.assert_called_once()

    def test_serial_open_raises(self):
        with self.assertRaises(RoombaConnectionError):
            _ = SerialRoomba("")

    @patch("serialroomba.controllers.serial.SerialController.connection")
    def test_serial_closed_raises(self, mock_connection):
        mock_connection.is_open = False
        with self.assertRaises(RoombaConnectionError):
            _ = SerialRoomba("")

    @patch("serialroomba.controllers.serial.SerialController.connection")
    @patch("serialroomba.controllers.serial.SerialController._pack_data")
    def test_send_command_converts_int(self, mock_pack_data, _):
        controller = SerialController("", 0, 0)
        controller.send_command(0, 0)
        mock_pack_data.assert_called_with(0, [0])

    @patch("serialroomba.controllers.serial.SerialController.connection")
    @patch("serialroomba.controllers.serial.SerialController.send_command")
    def test_send_sensor_request(self, mock_send_command, mock_connection):
        controller = SerialController("", 0, 0)
        mock_send_command.assert_not_called()
        mock_connection.read.assert_not_called()
        controller._send_sensor_request(0, 2)
        mock_send_command.assert_called_once
        mock_connection.read.assert_called_with(2)

    @patch("serialroomba.controllers.serial.SerialController.connection")
    @patch(
        "serialroomba.controllers.serial.SerialController._send_sensor_request",
        return_value=b"1",
    )
    def test_get_sensor_data(self, mock_send_sensor_request, _):
        controller = SerialController("", 0, 0)
        packet = SensorPacket(1, DataTypes.BOOL)
        _ = controller.get_sensor_data(packet)
        mock_send_sensor_request.assert_called_once
