from .controller import Controller


class CleaningMode:
    DEFAULT = 135
    MAX = 136
    SPOT = 134


class CleaningController(Controller):
    def start_default_cleaning(self) -> None:
        self.serial_controller.send_command(CleaningMode.DEFAULT)

    def start_max_cleaning(self) -> None:
        self.serial_controller.send_command(CleaningMode.MAX)

    def start_spot_cleaning(self) -> None:
        self.serial_controller.send_command(CleaningMode.SPOT)
