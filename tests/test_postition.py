from unittest import TestCase
from levelup.position import Position

class TestPositionInitWithCoordinates(TestCase):
   
    def test_init(self):
        coordinate_X = 5
        coordinate_Y = 5
        testobj = Position(coordinate_X,coordinate_Y)
        self.assertEqual(testobj.coordinate_X, coordinate_X)
        self.assertEqual(testobj.coordinate_Y, coordinate_Y)


    def test_init_wrong(self):
        coordinate_X = "bob"
        coordinate_Y = "sue"
        testobj = Position(coordinate_X,coordinate_Y)
        self.assertEqual(type(testobj.coordinate_X), int)
        self.assertEqual(type(testobj.coordinate_Y), int)
