from unittest import TestCase

from serialroomba.controllers.models.command import Command, CommandEnum
from serialroomba.controllers.serial import DataTypes


COMMAND_1_NAME = "Command 1"
COMMAND_1_SERIAL_COMMAND = 1
COMMAND_1_DATA_BYTES = DataTypes.BOOL


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
        self.assertEqual(SomeCommands.COMMAND_1.data_types, COMMAND_1_DATA_BYTES)
