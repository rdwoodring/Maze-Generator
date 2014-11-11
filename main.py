__author__ = 'rswoody'

from Maze import Maze

#generate 5 mazes
total_mazes = 5

maze_index = 0

while maze_index < total_mazes:
    maze = Maze(10, 10)
    maze.generate()

    maze.print_maze("maze" + str(maze_index + 1))

    maze_index += 1

print("Complete")