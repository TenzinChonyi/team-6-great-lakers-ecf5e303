from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position
from levelup.controller import Direction

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

    def test_valid_y_coordinate(self):
        map = GameMap()
        position = Position(2,9)
        self.assertTrue(map.validate_position(position))

    def test_calculate_move_north(self):
        map = GameMap()
        current_position = Position(0,0)
        direction = Direction.NORTH
        calculated_position = map.calculate_position(current_position, direction)
        self.assertEqual(calculated_position.coordinate_X, 0)
        self.assertEqual(calculated_position.coordinate_Y, 1)

    def test_calculate_move_south(self):
        map = GameMap()
        current_position = Position(0,1)
        direction = Direction.SOUTH
        calculated_position = map.calculate_position(current_position, direction)
        self.assertEqual(calculated_position.coordinate_X, 0)
        self.assertEqual(calculated_position.coordinate_Y, 0)

    def test_calculate_move_east(self):
        map = GameMap()
        current_position = Position(0,0)
        direction = Direction.EAST
        calculated_position = map.calculate_position(current_position, direction)
        self.assertEqual(calculated_position.coordinate_X, 1)
        self.assertEqual(calculated_position.coordinate_Y, 0)

    def test_calculate_move_west(self):
        map = GameMap()
        current_position = Position(1,0)
        direction = Direction.WEST
        calculated_position = map.calculate_position(current_position, direction)
        self.assertEqual(calculated_position.coordinate_X, 0)
        self.assertEqual(calculated_position.coordinate_Y, 0)
