from unittest.mock import patch
from unittest import TestCase

from serialroomba.controllers.mode import Mode
from serialroomba.serialroomba import SerialRoomba


@patch("serialroomba.controllers.SerialController._connect_serial")
@patch("serialroomba.controllers.SerialController.send_command")
class TestModeController(TestCase):
    def test_setter_calls_serial_controller(self, mock_send_command, _):
        roomba = SerialRoomba("/dev/null")
        mock_send_command.assert_called_once()  # Initializing the class already sets the mode

        roomba.mode_controller.current_mode = Mode.SAFE
        self.assertEqual(mock_send_command.call_count, 2)

    @patch("serialroomba.controllers.SerialController.get_sensor_data", return_value=0)
    def test_getter_calls_serial_controller(
        self, mock_get_sensor_data, mock_send_command, _
    ):
        roomba = SerialRoomba("/dev/null")
        mock_get_sensor_data.assert_not_called()

        _ = roomba.mode_controller.current_mode
        mock_get_sensor_data.assert_called_once()
