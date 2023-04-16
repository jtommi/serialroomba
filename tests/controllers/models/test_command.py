from unittest import TestCase

from serialroomba.controllers.models.command import Command, CommandEnum


COMMAND_1_NAME = "Command 1"
COMMAND_1_SERIAL_COMMAND = 1
COMMAND_1_DATA_BYTES = 2


class SomeCommands(CommandEnum):
    COMMAND_1 = Command(
        COMMAND_1_NAME,
        COMMAND_1_SERIAL_COMMAND,
        COMMAND_1_DATA_BYTES,
    )


class TestCommandEnum(TestCase):
    def test_command_properties(self):
        self.assertEqual(SomeCommands.COMMAND_1.name, COMMAND_1_NAME)
        self.assertEqual(
            SomeCommands.COMMAND_1.serial_command, COMMAND_1_SERIAL_COMMAND
        )
        self.assertEqual(
            SomeCommands.COMMAND_1.number_of_data_bytes, COMMAND_1_DATA_BYTES
        )
