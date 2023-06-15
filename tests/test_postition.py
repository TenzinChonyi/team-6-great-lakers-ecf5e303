from unittest import TestCase
from levelup.position import Position

class TestPositionInit(TestCase):
    def test_init(self):
        CoordinateX = 0
        CoordinateY = 0
        testobj = Position(CoordinateX,CoordinateY)
        self.assertEqual(testobj.CoordinateX, 0)
        self.assertEqual(testobj.CoordinateY, 0)
