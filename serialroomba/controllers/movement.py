from .controller import Controller
from .serial import SerialController


class MotorController(Controller):
    def __init__(
        self, serial_controller: SerialController, wheel_span_mm: float
    ) -> None:
        super().__init__(serial_controller)
        self._wheel_span_mm = wheel_span_mm
