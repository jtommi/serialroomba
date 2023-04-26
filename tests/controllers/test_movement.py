from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.movement import MovementCommand, MovementController


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
        self.assertEqual(self.movement_controller.velocity_total, 1)
        self.assertEqual(self.movement_controller.radius, 1)
        self.assertEqual(self.movement_controller.velocity_left_wheel, 1)
        self.assertEqual(self.movement_controller.velocity_right_wheel, 1)

        self.assertEqual(
            self.movement_controller.pwm_left_wheel, 0
        )  # Doesn't call get_sensor_data
        self.assertEqual(
            self.movement_controller.pwm_left_wheel, 0
        )  # Doesn't call get_sensor_data

        self.assertEqual(mock_get_sensor_data.call_count, 7)

    @patch("serialroomba.controllers.movement.MovementController.get_sensor_data")
    @patch("serialroomba.controllers.movement.MovementController.send_command")
    def test_normal_drive_byte_order(self, mock_send_command, mock_get_sensor_data):
        mock_get_sensor_data.return_value = 1

        self.movement_controller.velocity_total = 20
        mock_send_command.assert_called_with(MovementCommand.DRIVE, [20, 1])

        self.movement_controller.radius = 10
        mock_send_command.assert_called_with(MovementCommand.DRIVE, [1, 10])

        self.movement_controller.velocity_left_wheel = 20
        mock_send_command.assert_called_with(MovementCommand.DRIVE_DIRECT, [1, 20])

        self.movement_controller.velocity_right_wheel = 10
        mock_send_command.assert_called_with(MovementCommand.DRIVE_DIRECT, [10, 1])

    @patch("serialroomba.controllers.movement.MovementController.send_command")
    def test_pwm_byte_order(self, mock_send_command):
        self.movement_controller.pwm_left_wheel = 20
        self.movement_controller.pwm_right_wheel = 10
        mock_send_command.assert_called_with(MovementCommand.DRIVE_PWM, [10, 20])
