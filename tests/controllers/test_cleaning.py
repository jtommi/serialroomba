from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.cleaning import CleaningController, CleaningMode


class TestCleaningController(TestCase):
    def setUp(self) -> None:
        self.serial_mock = Mock()
        self.cleaning_controller = CleaningController(self.serial_mock)

    def test_setter_calls_serial_controller(self):
        self.cleaning_controller.current_cleaning_mode = CleaningMode.DEFAULT
        self.serial_mock.send_command.assert_called_once()

    @patch("serialroomba.controllers.cleaning.CleaningModeState.from_state_id")
    def test_getter_does_not_call_serial_controller(self, mock_from_state_id):
        self.serial_mock.get_sensor_data.return_value = b"1"
        _ = self.cleaning_controller.current_cleaning_mode
        self.serial_mock.get_sensor_data.assert_not_called()
