from unittest import TestCase

from serialroomba.controllers.models.state import State, StateEnum


class TestValidatorEnum(TestCase):
    def test_state_enum_raises_on_invalid_member(self):
        class ValidStateEnum(StateEnum):
            valid = State("Test", 1)
            also_valid = State("Test2", 1)

        _ = ValidStateEnum.valid  # Avoid linter complaining about unused class

        with self.assertRaises(TypeError):

            class InvalidStateEnum(StateEnum):
                valid = State("Test", 1)
                invalid = "Not a state"

            _ = InvalidStateEnum.valid  # Avoid linter complaining about unused class
