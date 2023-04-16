from unittest import TestCase

from serialroomba.controllers.models.sensor import Sensor, SensorEnum
from serialroomba.controllers.serial import DataTypes


SENSOR_1_NAME = "Sensor 1"
SENSOR_1_PACKET_ID = 1
SENSOR_1_DATA_TYPE = DataTypes.BOOL


class SomeSensors(SensorEnum):
    SENSOR_1 = Sensor(
        SENSOR_1_NAME,
        SENSOR_1_PACKET_ID,
        SENSOR_1_DATA_TYPE,
    )


class TestSensorEnum(TestCase):
    def test_sensor_properties(self):
        self.assertEqual(SomeSensors.SENSOR_1.name, SENSOR_1_NAME)
        self.assertEqual(SomeSensors.SENSOR_1.packet_id, SENSOR_1_PACKET_ID)
        self.assertEqual(SomeSensors.SENSOR_1.data_type, SENSOR_1_DATA_TYPE)
