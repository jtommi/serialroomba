from unittest import TestCase

from serialroomba.controllers.state import State, StateEnum


class TestStateEnum(TestCase):
    def test_state_enum_raises_on_invalid_member(self):
        class ValidTestStateEnum(StateEnum):
            valid = State("Test", 1, 1)
            also_valid = State("Test2", 1, 1)

        with self.assertRaises(TypeError):

            class InvalidTestStateEnum(StateEnum):
                valid = State("Test", 1, 1)
                invalid = "Not a state"
