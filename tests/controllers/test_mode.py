from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.mode import Mode, ModeController


class TestModeController(TestCase):
    def setUp(self) -> None:
        self.serial_mock = Mock()
        self.mode_controller = ModeController(self.serial_mock)

    def test_setter_calls_serial_controller(self):
        self.mode_controller.current_mode = Mode.SAFE
        self.serial_mock.send_command.assert_called_once()

    @patch("serialroomba.controllers.mode.Mode.from_state_id")
    def test_getter_calls_serial_controller(self, mock_from_state_id):
        self.serial_mock.get_sensor_data.return_value = b"1"
        _ = self.mode_controller.current_mode
        self.serial_mock.get_sensor_data.assert_called_once()
