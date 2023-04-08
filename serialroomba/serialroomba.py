from .controllers import (
    CleaningController,
    Mode,
    ModeController,
    MotorController,
    SerialController,
)
from .controllers import PowerSensor


class SerialRoomba:
    def __init__(
        self,
        port: str,
        baud_rate: int = 115200,
        time_out_s: float = 1.0,
        wheel_span_mm: float = 235.0,
    ):
        self.serial_controller = SerialController(
            port=port, baud_rate=baud_rate, time_out_s=time_out_s
        )

        self.mode_controller = ModeController(self.serial_controller)
        self.cleaning_controller = CleaningController(self.serial_controller)
        self.motor_controller = MotorController(
            self.serial_controller, wheel_span_mm=wheel_span_mm
        )
        self.power_sensor = PowerSensor(self.serial_controller)

        # sleep(1) #TODO Remove of uncomment
        self.mode_controller.current_mode = Mode.PASSIVE
