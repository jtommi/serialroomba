import unittest.mock as mock
from unittest import TestCase

from serialroomba.controllers.mode import Mode
from serialroomba.serialroomba import SerialRoomba


@mock.patch("serialroomba.controllers.SerialController._connect_serial")
@mock.patch("serialroomba.controllers.SerialController.send_command")
class TestModeController(TestCase):
    def test_setter_calls_serial_controller(self, mock_send_command, _):
        roomba = SerialRoomba("/dev/null")
        mock_send_command.assert_called_once()  # Initializing the class already sets the mode

        roomba.mode_controller.current_mode = Mode.SAFE
        self.assertEqual(mock_send_command.call_count, 2)

    @mock.patch(
        "serialroomba.controllers.SerialController.get_sensor_data", return_value=0
    )
    def test_getter_calls_serial_controller(
        self, mock_get_sensor_data, mock_send_command, _
    ):
        roomba = SerialRoomba("/dev/null")
        mock_get_sensor_data.assert_not_called()  # Initializing the class already sets the mode

        _ = roomba.mode_controller.current_mode
        mock_get_sensor_data.assert_called_once()  # Initializing the class already sets the mode
