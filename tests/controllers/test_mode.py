import unittest.mock as mock
from unittest import TestCase

from serialroomba.controllers.mode import Mode
from serialroomba.serialroomba import SerialRoomba


@mock.patch("serialroomba.controllers.SerialController._connect_serial")
class TestModeController(TestCase):
    @mock.patch("serialroomba.controllers.SerialController.send_command")
    def test_setter_writes_to_serial(self, mock_send_command, _):
        roomba = SerialRoomba("/dev/null")
        mock_send_command.assert_called_once()  # Initializing the class already sets the mode

        roomba.mode_controller.current_mode = Mode.SAFE
        self.assertEqual(mock_send_command.call_count, 2)

