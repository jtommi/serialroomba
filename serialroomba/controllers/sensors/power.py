from .sensor import Sensor
from .packet import SensorPacket


class PowerPackets:
    BATTERY_CAPACITY = SensorPacket(26, 2, False)
    BATTERY_CHARGE = SensorPacket(25, 2, False)
    BATTERY_TEMPERATURE = SensorPacket(24, 1, True)
    CHARGING_STATE = SensorPacket(21, 1, False)
    CURRENT = SensorPacket(23, 3, True)
    VOLTAGE = SensorPacket(22, 2, True)


class PowerSensor(Sensor):
    @property
    def battery_voltage(self) -> int:
        return self.get_sensor_data(PowerPackets.VOLTAGE)

    @property
    def battery_current(self) -> int:
        return self.get_sensor_data(PowerPackets.CURRENT)

    @property
    def battery_charge(self) -> int:
        return self.get_sensor_data(PowerPackets.BATTERY_CHARGE)

    @property
    def battery_capacity(self) -> int:
        return self.get_sensor_data(PowerPackets.BATTERY_CAPACITY)

    @property
    def battery_temperature(self) -> int:
        return self.get_sensor_data(PowerPackets.BATTERY_TEMPERATURE)

    @property
    def is_charging(self) -> bool:
        charging_state = self.get_sensor_data(PowerPackets.CHARGING_STATE)
        return bool(charging_state)
