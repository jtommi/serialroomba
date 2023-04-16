from .controller import Controller
from .models.command import Command, CommandEnum
from .models.state import State, StateEnum


class CleaningMode(CommandEnum):
    DEFAULT = Command("Default", 135)
    MAX = Command("Max", 136)
    SPOT = Command("Spot", 134)


class CleaningModeState(StateEnum):
    DEFAULT = State("Default", 135)
    MAX = State("Max", 136)
    SPOT = State("Spot", 134)


class CleaningController(Controller):
    _last_set_cleaning_mode: StateEnum | None = None

    @property
    def current_cleaning_mode(self) -> StateEnum | None:
        """Last set cleaning mode, the Roomba doesn't provide the current cleaning mode"""
        return self._last_set_cleaning_mode

    @current_cleaning_mode.setter
    def current_cleaning_mode(self, cleaning_mode: CleaningMode) -> None:
        self._last_set_cleaning_mode = CleaningModeState.from_state_id(
            cleaning_mode.serial_command
        )
        self.serial_controller.send_command(cleaning_mode.serial_command)
