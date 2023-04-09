from unittest import TestCase
from unittest.mock import Mock

from serialroomba.controllers.mode import Mode, ModeController


class TestModeController(TestCase):
    def setUp(self) -> None:
        self.serial_mock = Mock()
        self.mode_controller = ModeController(self.serial_mock)

    def test_setter_calls_serial_controller(self):
        self.mode_controller.current_mode = Mode.SAFE
        self.serial_mock.send_command.assert_called_once()

    def test_getter_calls_serial_controller(self):
        self.serial_mock.get_sensor_data.return_value = 1
        _ = self.mode_controller.current_mode
        self.serial_mock.get_sensor_data.assert_called_once()
