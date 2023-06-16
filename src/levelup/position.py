class Position:
    coordinate_X = ""
    coordinate_Y = ""

    def __init__(self, coordinate_X, coordinate_Y):
       if type(coordinate_X) != int: coordinate_X =0
       if type(coordinate_Y) != int: coordinate_Y =0
       self.coordinate_X = coordinate_X
       self.coordinate_Y = coordinate_Y


