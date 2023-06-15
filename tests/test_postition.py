from unittest import TestCase
from levelup.position import Position

class TestPositionInitWithCoordinates(TestCase):
   
    def test_init(self):
        CoordinateX = 5
        CoordinateY = 5
        testobj = Position(CoordinateX,CoordinateY)
        self.assertEqual(testobj.CoordinateX, CoordinateX)
        self.assertEqual(testobj.CoordinateY, CoordinateY)


    def test_init_wrong(self):
        CoordinateX = "bob"
        CoordinateY = "sue"
        testobj = Position(CoordinateX,CoordinateY)
        self.assertEqual(type(testobj.CoordinateX), int)
        self.assertEqual(type(testobj.CoordinateY), int)


