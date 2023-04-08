import unittest

from serialroomba.serialroomba import SerialRoomba


class TestSerialRoomba(unittest.TestCase):
    def test_serialroomba(self):
        roomba = SerialRoomba("COM1")

        self.assertTrue(roomba)
