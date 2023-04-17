from .models.command import Command, CommandEnum
from .controller import Controller
from .serial import SerialController


class MovementCommand(CommandEnum):
    DRIVE = Command("Drive", 137, 4)
    DRIVE_DIRECT = Command("Drive direct", 145, 4)
    DRIVE_PWM = Command("Drive PWM", 146, 4)


class MovementController(Controller):
    def __init__(
        self, serial_controller: SerialController, wheel_span_mm: float
    ) -> None:
        super().__init__(serial_controller)
        self._wheel_span_mm = wheel_span_mm
