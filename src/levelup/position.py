class Position:
    CoordinateX = ""
    CoordinateY = ""

    def __init__(self, CoordinateX, CoordinateY):
       if type(CoordinateX) != int: CoordinateX =0
       if type(CoordinateY) != int: CoordinateY =0
       self.CoordinateX = CoordinateX
       self.CoordinateY = CoordinateY


