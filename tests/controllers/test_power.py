from unittest import TestCase
from unittest.mock import Mock, patch

from serialroomba.controllers.power import ChargingState, PowerController


class TestPowerController(TestCase):
    @patch("serialroomba.controllers.power.PowerController.get_sensor_data")
    def test_getters(self, mock_get_sensor_data):
        serial_controller_mock = Mock()
        power_controller = PowerController(serial_controller_mock)
        mock_get_sensor_data.return_value = 1

        self.assertEqual(power_controller.battery_capacity_mAh, 1)
        self.assertEqual(power_controller.battery_charge_mAh, 1)
        self.assertEqual(power_controller.battery_current_mA, 1)
        self.assertEqual(power_controller.battery_temperature_deg_C, 1)
        self.assertEqual(power_controller.battery_voltage_mV, 1)
        self.assertEqual(
            power_controller.battery_charging_state,
            ChargingState.RECONDITIONING_CHARGING,
        )
        self.assertEqual(power_controller.battery_is_charging, True)
        self.assertEqual(power_controller.internal_charger_available, True)
        self.assertEqual(power_controller.base_charger_available, False)

        mock_get_sensor_data.return_value = 0
        self.assertEqual(power_controller.battery_is_charging, False)
