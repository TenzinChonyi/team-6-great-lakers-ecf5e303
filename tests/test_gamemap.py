from unittest import TestCase
from levelup.gamemap import GameMap
from levelup.position import Position

class TestMapInitDetails(TestCase):
    def test_init(self):
        map = GameMap()
        map.position = Position(0,0)

