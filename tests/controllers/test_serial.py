import unittest.mock as mock
from unittest import TestCase

from serialroomba.controllers.serial import SerialController
from serialroomba.exceptions import RoombaConnectionError
from serialroomba.serialroomba import SerialRoomba


class TestSerialController(TestCase):
    @mock.patch("serialroomba.controllers.serial.SerialController.connection")
    def test_serial_open_is_called(self, mock_connection):
        self.assertEqual(mock_connection.open.call_count, 0)
        _ = SerialRoomba("/dev/null")
        mock_connection.open.assert_called_once()

    def test_serial_open_raises(self):
        with self.assertRaises(RoombaConnectionError):
            _ = SerialRoomba("")

    @mock.patch("serialroomba.controllers.serial.SerialController.connection")
    def test_serial_closed_raises(self, mock_connection):
        mock_connection.is_open = False
        with self.assertRaises(RoombaConnectionError):
            _ = SerialRoomba("")

    @mock.patch("serialroomba.controllers.serial.SerialController.connection")
    @mock.patch("serialroomba.controllers.serial.SerialController._pack_data")
    def test_send_command_converts_int(self, mock_pack_data, _):
        controller = SerialController("", 0, 0)
        controller.send_command(0, 0)
        mock_pack_data.assert_called_with(0, [0])
