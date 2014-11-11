__author__ = 'rswoody'

from random import shuffle
from os import listdir
from os.path import isfile, join

from Direction import Direction
from Room import Room

class Maze:
    def __init__(self, width, height):
        h_count = 0
        self.width = width
        self.height = height
        self.rooms = []

        while h_count < self.height:
            w_count = 0

            while w_count < self.width:
                room = Room(w_count, h_count)
                self.rooms.append(room)

                #print("Generating room at " + str(w_count) + ", " + str(h_count))

                w_count += 1

            h_count += 1

    def generate(self, current_x = 0, current_y = 0):
        current_room = next(room for room in self.rooms if room.x == current_x and room.y == current_y)
        current_room.visited = True
        directions = [Direction.north, Direction.east, Direction.south, Direction.west]
        shuffle(directions)
        for direction in directions:
            if direction == Direction.north:
                if self.room_exists(current_room.x, current_room.y - 1) and current_room.exits[Direction.north] == False:
                    next_room = next(room for room in self.rooms if room.x == current_room.x and room.y == current_room.y - 1)
                    if next_room.visited == False:
                        current_room.exits[Direction.north] = True
                        next_room.exits[Direction.south] = True
                        self.generate(next_room.x, next_room.y)
            elif direction == Direction.east:
                if self.room_exists(current_room.x + 1, current_room.y) and current_room.exits[Direction.east] == False:
                    next_room = next(room for room in self.rooms if room.x == current_room.x + 1 and room.y == current_room.y)
                    if next_room.visited == False:
                        current_room.exits[Direction.east] = True
                        next_room.exits[Direction.west] = True
                        self.generate(next_room.x, next_room.y)
            elif direction == Direction.south:
                if self.room_exists(current_room.x, current_room.y + 1) and current_room.exits[Direction.south] == False:
                    next_room = next(room for room in self.rooms if room.x == current_room.x and room.y == current_room.y + 1)
                    if next_room.visited == False:
                        current_room.exits[Direction.south] = True
                        next_room.exits[Direction.north] = True
                        self.generate(next_room.x, next_room.y)
            elif direction == Direction.west:
                if self.room_exists(current_room.x - 1, current_room.y) and current_room.exits[Direction.south] == False:
                    next_room = next(room for room in self.rooms if room.x == current_room.x - 1 and room.y == current_room.y)
                    if next_room.visited == False:
                        current_room.exits[Direction.west] = True
                        next_room.exits[Direction.east] = True
                        self.generate(next_room.x, next_room.y)


    def room_exists(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False

    def print_maze(self, file_name):
        fo = open("Mazes/" + file_name + ".txt", "w")
        #fo.write("test")
        maze_string = ""
        #draw top row
        count = 0

        y_count = 0

        while y_count < self.height:
            rooms = []
            for room in self.rooms:
                if room.y == y_count:
                    rooms.append(room)

            for room in rooms:
                if room.x == 0:
                    maze_string += "+"

                if room.exits[Direction.north]:
                    maze_string += " +"
                else:
                    maze_string += "-+"

            maze_string += "\r\n"

            for room in rooms:
                if room.x == 0:
                    maze_string += "|"

                if room.exits[Direction.east]:
                    maze_string += "  "
                else:
                    maze_string += " |"

            maze_string += "\r\n"

            y_count += 1

        count = 0
        maze_string += "+"
        while count < self.width:
            maze_string += "-+"
            count += 1

        fo.write(maze_string)

        fo.close()