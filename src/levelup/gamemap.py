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

    def calculate_position(self, current_position, direction):
        new_position = Position(current_position.coordinate_X, current_position.coordinate_Y);
        match (direction):
            case direction.NORTH:
                new_position.coordinate_Y += 1
            case direction.SOUTH:
                new_position.coordinate_Y -= 1            
            case direction.EAST:
                new_position.coordinate_X += 1            
            case direction.WEST:
                new_position.coordinate_X -= 1            

        if self.validate_position(new_position):
            return new_position

        return current_position