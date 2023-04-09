from serialroomba.controllers.controller import Controller
from serialroomba.controllers.serial import DataTypes
from serialroomba.controllers.state import State, StateEnum
from .packet import SensorPacket


class PowerPackets:
    BATTERY_CAPACITY = SensorPacket(26, DataTypes.UNSIGNED_TWO_BYTES)
    BATTERY_CHARGE = SensorPacket(25, DataTypes.UNSIGNED_TWO_BYTES)
    BATTERY_TEMPERATURE = SensorPacket(24, DataTypes.SIGNED_BYTE)
    CHARGING_STATE = SensorPacket(21, DataTypes.UNSIGNED_BYTE)
    CURRENT = SensorPacket(23, DataTypes.SIGNED_TWO_BYTES)
    VOLTAGE = SensorPacket(22, DataTypes.UNSIGNED_TWO_BYTES)


class ChargingState(StateEnum):
    NOT_CHARGING = State("Not charging", None, 0)
    RECONDITIONING_CHARGING = State("Reconditioning charging", None, 1)
    FULL_CHARGING = State("Full charging", None, 2)
    TRICKLE_CHARGING = State("Trickle charging", None, 3)
    WAITING = State("Waiting", None, 4)
    CHARGING_FAULT_CONDITION = State("Waiting", None, 5)


class PowerController(Controller):
    @property
    def battery_voltage_mV(self) -> int:
        return self.get_sensor_data(PowerPackets.VOLTAGE)

    @property
    def battery_current_mA(self) -> int:
        return self.get_sensor_data(PowerPackets.CURRENT)

    @property
    def battery_charge_mAh(self) -> int:
        return self.get_sensor_data(PowerPackets.BATTERY_CHARGE)

    @property
    def battery_capacity_mAh(self) -> int:
        return self.get_sensor_data(PowerPackets.BATTERY_CAPACITY)

    @property
    def battery_temperature_deg_C(self) -> int:
        return self.get_sensor_data(PowerPackets.BATTERY_TEMPERATURE)

    @property
    def battery_charging_state(self) -> StateEnum:
        charging_state_id = self.get_sensor_data(PowerPackets.CHARGING_STATE)
        return ChargingState.from_state_id(charging_state_id)

    @property
    def battery_is_charging(self) -> bool:
        charging_state = self.get_sensor_data(PowerPackets.CHARGING_STATE)
        if charging_state in [
            ChargingState.NOT_CHARGING,
            ChargingState.CHARGING_FAULT_CONDITION,
        ]:
            return False
        return True
