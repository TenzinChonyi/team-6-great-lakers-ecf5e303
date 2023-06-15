from unittest import TestCase
from levelup.position import Position

class TestPositionInitBottomLeftOfMap(TestCase):
    def test_init(self):
        CoordinateX = 0
        CoordinateY = 0
        testobj = Position(CoordinateX,CoordinateY)
        self.assertEqual(testobj.CoordinateX, 0)
        self.assertEqual(testobj.CoordinateY, 0)

class TestPositionInitMiddleOfMap(TestCase):
    def test_init(self):
        CoordinateX = 5
        CoordinateY = 5
        testobj = Position(CoordinateX,CoordinateY)
        self.assertEqual(testobj.CoordinateX, 5)
        self.assertEqual(testobj.CoordinateY, 5)


class TestPositionInitNonNumberInput(TestCase):
    def test_init(self):
        CoordinateX = "bob"
        CoordinateY = "sue"
        testobj = Position(CoordinateX,CoordinateY)
        self.assertEqual(type(testobj.CoordinateX), int)
        self.assertEqual(type(testobj.CoordinateY), int)


