from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.environment import EnvironmentController, InfraredOpCodes


class TestEnvironmentController(TestCase):
    @patch("serialroomba.controllers.environment.EnvironmentController.get_sensor_data")
    def test_getters(self, mock_get_sensor_data):
        serial_controller_mock = Mock()
        environment_controller = EnvironmentController(serial_controller_mock)
        mock_get_sensor_data.return_value = 1

        self.assertEqual(environment_controller.wall_detected, True)
        self.assertEqual(environment_controller.cliff_left_detected, True)
        self.assertEqual(environment_controller.cliff_front_left_detected, True)
        self.assertEqual(environment_controller.cliff_front_right_detected, True)
        self.assertEqual(environment_controller.cliff_right_detected, True)
        self.assertEqual(environment_controller.virtual_wall_detected, True)
        self.assertEqual(environment_controller.wall_signal, 1)
        self.assertEqual(environment_controller.cliff_left_signal, 1)
        self.assertEqual(environment_controller.cliff_front_left_signal, 1)
        self.assertEqual(environment_controller.cliff_front_right_signal, 1)
        self.assertEqual(environment_controller.cliff_right_signal, 1)
        self.assertEqual(environment_controller.light_bumper_left_signal, 1)
        self.assertEqual(environment_controller.light_bumper_front_left_signal, 1)
        self.assertEqual(environment_controller.light_bumper_center_left_signal, 1)
        self.assertEqual(environment_controller.light_bumper_center_right_signal, 1)
        self.assertEqual(environment_controller.light_bumper_front_right_signal, 1)
        self.assertEqual(environment_controller.light_bumper_right_signal, 1)

        mock_get_sensor_data.return_value = 63
        self.assertEqual(environment_controller.light_bumper_left_detected, True)
        self.assertEqual(environment_controller.light_bumper_front_left_detected, True)
        self.assertEqual(environment_controller.light_bumper_center_left_detected, True)
        self.assertEqual(
            environment_controller.light_bumper_center_right_detected, True
        )
        self.assertEqual(environment_controller.light_bumper_front_right_detected, True)
        self.assertEqual(environment_controller.light_bumper_right_detected, True)
        self.assertEqual(environment_controller.bumper_left_activate, True)
        self.assertEqual(environment_controller.bumper_right_activate, True)
        self.assertEqual(environment_controller.wheel_left_dropped, True)
        self.assertEqual(environment_controller.wheel_right_dropped, True)

        mock_get_sensor_data.return_value = 129
        self.assertEqual(
            environment_controller.infrared_opcode_left, InfraredOpCodes.IR_REMOTE_LEFT
        )
        self.assertEqual(
            environment_controller.infrared_opcode_right, InfraredOpCodes.IR_REMOTE_LEFT
        )
