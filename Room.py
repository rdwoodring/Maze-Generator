__author__ = 'rswoody'

from Direction import Direction

class Room:
    def __init__(self, x, y):
        #self.n_exit, self.e_exit, self.s_exit, self.w_exit = False, False, False, False
        self.exits = {Direction.north: False, Direction.east: False, Direction.south: False, Direction.west: False}
        self.x, self.y = x, y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        data = "x: " + str(self.x)
        return data

    def is_dead_end(self):
        dead_end = True
        for key, value in self.exits.items():
            if not value:
                dead_end = False

        return dead_end