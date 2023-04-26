from unittest import TestCase
from unittest.mock import Mock

from serialroomba.controllers.controller import Controller
from serialroomba.controllers.models.command import Command, CommandEnum
from serialroomba.controllers.models.sensor import Sensor
from serialroomba.controllers.serial import DataTypes

SENSOR = Sensor("Test sensor", 1, DataTypes.UNSIGNED_BYTE)


class TestController(TestCase):
    def setUp(self) -> None:
        self.serial_mock = Mock()
        self.controller = Controller(self.serial_mock)

    def test_bit_is_set(self):
        self.assertTrue(self.controller.check_bit_is_set(1, 0))
        self.assertFalse(self.controller.check_bit_is_set(1, 1))
        self.assertTrue(self.controller.check_bit_is_set(2, 1))
        self.assertFalse(self.controller.check_bit_is_set(2, 0))

    def test_get_sensor_data_unpacking(self):
        self.serial_mock.get_sensor_data.return_value = bytes([9])
        result = self.controller.get_sensor_data(SENSOR)
        self.assertEqual(result, 9)

    def test_send_command_converts_int(self):
        class TestEnum(CommandEnum):
            TEST = Command("test", 2)

        self.controller.send_command(command=TestEnum.TEST, data=1)
        self.serial_mock.send_command.assert_called_with(2, [1], [])
