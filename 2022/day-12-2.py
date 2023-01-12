import os
import sys
import time

sys.setrecursionlimit(10000)

with open('day-12.data') as f:
    data = [line.rstrip('\n') for line in f]

MAX_INT = 10000

width = len(data[0])
height = len(data)

height_map = []
min_steps_map = {}
previous_point_map = {}

start_points = []


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.y * width + self.x

    def is_valid(self):
        return 0 <= self.x < width and 0 <= self.y < height

    def __str__(self):
        return f'{self.x} {self.y}'

    def get_value(self) -> int:
        return height_map[self.y][self.x]

    def add(self, x, y):
        return Point(self.x + x, self.y + y)

    def add_point(self, point):
        return Point(self.x + point.x, self.y + point.y)


unvisited = set()

for i in range(height):
    height_map.append([])

    for j in range(width):
        c = data[i][j]
        if c == 'S':
            c = 'a'
        elif c == 'E':
            finish = Point(j, i)
            c = 'z'

        height_map[i].append(ord(c) - ord('a'))
        unvisited.add(Point(j, i))

        if c == 'a':
            start_points.append(Point(j, i))

moves = [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)]


def print_map(min_path: list = None):
    os.system('clear')
    for y in range(height):
        for x in range(width):
            if min_path:
                if Point(x, y) in min_path:
                    print('\033[96m\033[1m', end='')
            elif Point(x, y) == current_point:
                print('\033[46m\033[1m', end='')
            elif Point(x, y) not in unvisited:
                print('\033[96m\033[1m', end='')

            print(data[y][x], end='')
            print('\033[0m', end='')
        print()


path = []
min_steps_map[finish] = 0
current_point: Point = finish
i = 0
while True:
    new_steps = min_steps_map[current_point] + 1

    # evaluate neighbors
    for move in moves:
        new_point = current_point.add_point(move)
        if new_point in unvisited and new_point.get_value() >= (current_point.get_value() - 1):
            if new_point not in min_steps_map or min_steps_map[new_point] > new_steps:
                min_steps_map[new_point] = new_steps
                previous_point_map[new_point] = current_point

    if current_point in unvisited:
        unvisited.remove(current_point)

    next_current_point = None
    min_new_steps = MAX_INT
    for point in unvisited:
        if point in min_steps_map:
            if min_steps_map[point] < min_new_steps:
                min_new_steps = min_steps_map[point]
                next_current_point = point

    i += 1
    if i == 20:
        print_map()
        print(f'{current_point} -> {new_steps}')
        time.sleep(0.01)
        i = 0

    if not next_current_point:
        break

    current_point = next_current_point

print_map()

min_steps = MAX_INT
start_point = None
for point in start_points:
    if point in min_steps_map and min_steps_map[point] < min_steps:
        min_steps = min_steps_map[point]
        start_point = point

min_path = [start_point]
path_point = start_point
while True:
    if start_point not in previous_point_map:
        break

    start_point = previous_point_map[start_point]
    min_path.append(start_point)

print_map(min_path)

print(min_steps)
