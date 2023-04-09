from unittest import TestCase
from unittest.mock import Mock

from serialroomba.controllers.sensors.power import ChargingState, PowerController


class TestPowerController(TestCase):
    def test_getters(self):
        serial_controller_mock = Mock()
        serial_controller_mock.get_sensor_data.return_value = 1
        power_controller = PowerController(serial_controller_mock)

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

        serial_controller_mock.get_sensor_data.return_value = 0
        self.assertEqual(power_controller.battery_is_charging, False)
