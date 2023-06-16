from levelup.position import Position

class GameMap:
    position = Position(0,0)
    move_count = 0
    def __init__(self):
        pass

    def validate_position(self, position):
        if position.coordinate_X > 9 or position.coordinate_X < 0:
            return False
        elif position.coordinate_Y > 9 or position.coordinate_Y < 0:
            return False
        return True