from .controller import Controller
from .models.command import Command, CommandEnum
from .models.sensor import Sensor, SensorEnum
from .serial import DataTypes, SerialController


class MovementCommand(CommandEnum):
    DRIVE = Command("Drive", 137, 4)
    DRIVE_DIRECT = Command("Drive direct", 145, 4)
    DRIVE_PWM = Command("Drive PWM", 146, 4)


class MovementSensor(SensorEnum):
    DISTANCE = Sensor("Distance", 19, DataTypes.SIGNED_TWO_BYTES)
    ANGLE = Sensor("Angle", 20, DataTypes.SIGNED_TWO_BYTES)
    VELOCITY = Sensor("Velocity", 39, DataTypes.SIGNED_TWO_BYTES)
    RADIUS = Sensor("Radius", 40, DataTypes.SIGNED_TWO_BYTES)
    VELOCITY_RIGHT = Sensor("Velocity right", 41, DataTypes.SIGNED_TWO_BYTES)
    VELOCITY_LEFT = Sensor("Velocity left", 42, DataTypes.SIGNED_TWO_BYTES)
    ENCODER_COUNTS_LEFT = Sensor(
        "Encoder counts left", 43, DataTypes.UNSIGNED_TWO_BYTES
    )
    ENCODER_COUNTS_RIGHT = Sensor(
        "Encoder counts right", 44, DataTypes.UNSIGNED_TWO_BYTES
    )
    MOTOR_CURRENT_LEFT = Sensor("Motor current left", 54, DataTypes.SIGNED_TWO_BYTES)
    MOTOR_CURRENT_RIGHT = Sensor("Motor current right", 55, DataTypes.SIGNED_TWO_BYTES)
    STASIS = Sensor("Statis", 58, DataTypes.BOOL)


class MovementController(Controller):
    def __init__(
        self, serial_controller: SerialController, wheel_span_mm: float
    ) -> None:
        super().__init__(serial_controller)
        self._wheel_span_mm = wheel_span_mm

    @property
    def motor_left_current_mA(self) -> int:
        return self.get_sensor_data(MovementSensor.MOTOR_CURRENT_LEFT)

    @property
    def motor_right_current_mA(self) -> int:
        return self.get_sensor_data(MovementSensor.MOTOR_CURRENT_RIGHT)

    @property
    def is_moving(self) -> bool:
        return not self.get_sensor_data(MovementSensor.STASIS)  # type: ignore
