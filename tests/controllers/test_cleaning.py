from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.cleaning import CleaningController, CleaningMode


class TestCleaningController(TestCase):
    def setUp(self) -> None:
        self.serial_mock = Mock()
        self.cleaning_controller = CleaningController(self.serial_mock)

    def test_setter_calls_serial_controller(self):
        self.cleaning_controller.current_cleaning_mode = CleaningMode.DEFAULT
        self.cleaning_controller.side_brush_pwm = 0
        self.cleaning_controller.main_brush_pwm = 0
        self.cleaning_controller.vacuum_pwm = 0
        self.assertEqual(self.serial_mock.send_command.call_count, 4)

    @patch("serialroomba.controllers.cleaning.CleaningModeState.from_state_id")
    def test_getter_does_not_call_serial_controller(self, mock_from_state_id):
        self.serial_mock.get_sensor_data.return_value = b"1"
        _ = self.cleaning_controller.current_cleaning_mode
        self.serial_mock.get_sensor_data.assert_not_called()

    @patch("serialroomba.controllers.cleaning.CleaningController.get_sensor_data")
    def test_getters(self, mock_get_sensor_data):
        mock_get_sensor_data.return_value = 1

        self.assertEqual(self.cleaning_controller.dirt_detect_level, 1)
        self.assertEqual(self.cleaning_controller.main_brush_current_mA, 1)
        self.assertEqual(self.cleaning_controller.side_brush_current_mA, 1)
        self.assertEqual(self.cleaning_controller.side_brush_pwm, None)
        self.assertEqual(self.cleaning_controller.main_brush_pwm, None)
        self.assertEqual(self.cleaning_controller.vacuum_pwm, None)

    def test_vacuum_setter_raises_on_bad_value(self):
        with self.assertRaises(ValueError):
            self.cleaning_controller.vacuum_pwm = 200
