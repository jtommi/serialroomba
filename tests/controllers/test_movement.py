from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.movement import MovementController


class TestMovementController(TestCase):
    def setUp(self) -> None:
        self.serial_mock = Mock()
        self.movement_controller = MovementController(self.serial_mock, wheel_span_mm=1)

    @patch("serialroomba.controllers.movement.MovementController.get_sensor_data")
    def test_getters(self, mock_get_sensor_data):
        mock_get_sensor_data.return_value = 1

        self.assertEqual(self.movement_controller.motor_left_current_mA, 1)
        self.assertEqual(self.movement_controller.motor_right_current_mA, 1)
        self.assertFalse(self.movement_controller.is_moving)
