from unittest import TestCase

from serialroomba.controllers.state import State, StateEnum


state_1_name = "State 1"
state_1_command = 1
state_1_state_id = 1
state_2_name = "State 2"
state_2_command = 2
state_2_state_id = 2
invalid_state_id = 3


class SomeStates(StateEnum):
    STATE_1 = State(
        state_1_name,
        state_1_command,
        state_1_state_id,
    )
    STATE_2 = State(
        state_2_name,
        state_2_command,
        state_2_state_id,
    )


class TestStateEnum(TestCase):
    def test_state_enum_raises_on_invalid_member(self):
        class ValidStateEnum(StateEnum):
            valid = State("Test", 1, 1)
            also_valid = State("Test2", 1, 1)

        _ = ValidStateEnum.valid  # Avoid linter complaining about unused class

        with self.assertRaises(TypeError):

            class InvalidStateEnum(StateEnum):
                valid = State("Test", 1, 1)
                invalid = "Not a state"

            _ = InvalidStateEnum.valid  # Avoid linter complaining about unused class

    def test_from_state_id(self):
        state = SomeStates.from_state_id(state_2_state_id)
        self.assertEqual(SomeStates.STATE_2, state)

    def test_from_state_id_raises(self):
        with self.assertRaises(KeyError):
            _ = SomeStates.from_state_id(invalid_state_id)

    def test_state_properties(self):
        self.assertEqual(SomeStates.STATE_1.name, state_1_name)
        self.assertEqual(SomeStates.STATE_1.command, state_1_command)
        self.assertEqual(SomeStates.STATE_1.state_id, state_1_state_id)
