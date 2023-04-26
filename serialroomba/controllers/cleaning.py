from .controller import Controller
from .models.command import Command, CommandEnum
from .models.sensor import Sensor, SensorEnum
from .models.state import State, StateEnum
from .serial import DataTypes


class CleaningMode(CommandEnum):
    DEFAULT = Command("Default", 135)
    MAX = Command("Max", 136)
    SPOT = Command("Spot", 134)


class CleaningModeState(StateEnum):
    DEFAULT = State("Default", 135)
    MAX = State("Max", 136)
    SPOT = State("Spot", 134)


class CleaningSensor(SensorEnum):
    DIRT_DETECT = Sensor("Dirt detect", 15, DataTypes.UNSIGNED_BYTE)
    MAIN_BRUSH_MOTOR_CURRENT = Sensor(
        "Main brush motor current", 56, DataTypes.SIGNED_TWO_BYTES
    )
    SIDE_BRUSH_MOTOR_CURRENT = Sensor(
        "Side brush motor current", 57, DataTypes.SIGNED_TWO_BYTES
    )


class CleaningMotorCommand(CommandEnum):
    MOTORS = Command("Motors", 138, DataTypes.UNSIGNED_BYTE)
    PWM_MOTORS = Command(
        "PWM Motors",
        144,
        [DataTypes.SIGNED_BYTE, DataTypes.SIGNED_BYTE, DataTypes.UNSIGNED_BYTE],
    )


class CleaningController(Controller):
    _last_set_cleaning_mode: StateEnum | None = None
    _last_set_side_brush_pwm: int | None = None
    _last_set_main_brush_pwm: int | None = None
    _last_set_vacuum_pwm: int | None = None

    @property
    def current_cleaning_mode(self) -> StateEnum | None:
        """Last set cleaning mode, the Roomba doesn't provide the current cleaning mode"""
        return self._last_set_cleaning_mode

    @current_cleaning_mode.setter
    def current_cleaning_mode(self, cleaning_mode: CleaningMode) -> None:
        self._last_set_cleaning_mode = CleaningModeState.from_state_id(
            cleaning_mode.serial_command
        )
        self.send_command(cleaning_mode)

    @property
    def dirt_detect_level(self) -> int:
        return self.get_sensor_data(CleaningSensor.DIRT_DETECT)

    @property
    def main_brush_current_mA(self) -> int:
        return self.get_sensor_data(CleaningSensor.MAIN_BRUSH_MOTOR_CURRENT)

    @property
    def side_brush_current_mA(self) -> int:
        return self.get_sensor_data(CleaningSensor.SIDE_BRUSH_MOTOR_CURRENT)

    @property
    def side_brush_pwm(self) -> int | None:
        """Last set side brush PWM, the Roomba doesn't provide the current PWM"""
        return self._last_set_side_brush_pwm

    @side_brush_pwm.setter
    def side_brush_pwm(self, pwm: int) -> None:
        self._last_set_side_brush_pwm = pwm
        self.send_command(CleaningMotorCommand.PWM_MOTORS, [0, pwm, 0])

    @property
    def main_brush_pwm(self) -> int | None:
        """Last set side brush PWM, the Roomba doesn't provide the current PWM"""
        return self._last_set_side_brush_pwm

    @main_brush_pwm.setter
    def main_brush_pwm(self, pwm: int) -> None:
        self._last_set_main_brush_pwm = pwm
        self.send_command(CleaningMotorCommand.PWM_MOTORS, [pwm, 0, 0])

    @property
    def vacuum_pwm(self) -> int | None:
        """Last set vacuum PWM, the Roomba doesn't provide the current PWM"""
        return self._last_set_vacuum_pwm

    @vacuum_pwm.setter
    def vacuum_pwm(self, pwm: int) -> None:
        if pwm > 127:
            raise ValueError(
                f"Vacuum PWM must be between 0 and 127. Value provided: {pwm}"
            )
        self._last_set_vacuum_pwm = pwm
        self.send_command(CleaningMotorCommand.PWM_MOTORS, [0, 0, pwm])
