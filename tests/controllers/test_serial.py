import unittest.mock as mock
from unittest import TestCase

from serialroomba.controllers.mode import Mode
from serialroomba.serialroomba import SerialRoomba


@mock.patch("serialroomba.controllers.serial.SerialController.connection")
class TestSerialController(TestCase):
    def test_serial_open_is_called(self, mock_connection):
        self.assertEqual(mock_connection.open.call_count, 0)
        _ = SerialRoomba("/dev/null")
        mock_connection.open.assert_called_once()
