from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position

class TestMapInitDetails(TestCase):
    def test_init_position(self):
        map = GameMap()
        self.assertEqual(map.position.coordinate_X, 0)
        self.assertEqual(map.position.coordinate_Y, 0)

    def test_init_move_count(self):
        map = GameMap()
        self.assertEqual(map.move_count, 0)

    def test_valid_x_coordinate(self):
        map = GameMap()
        position = Position(-2,0)
        self.assertFalse(map.validate_position(position))