import math
import os
import time
from enum import Enum

with open('day-14.data') as f:
    data = [line.rstrip('\n') for line in f]

width = 1000
height = 1000

m = []


class Field(Enum):
    EMPTY = 0
    ROCK = 1
    SAND = 2


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
        return f'{self.x} × {self.y}'

    def get_value(self):
        return m[self.y][self.x]

    def add(self, x, y):
        return Point(self.x + x, self.y + y)

    def add_point(self, point):
        return Point(self.x + point.x, self.y + point.y)


for i in range(height):
    m.append([])

    for j in range(width):
        m[i].append(Field.EMPTY)

for line in data:
    points = [Point(int(x), int(y)) for x, y in (text.split(',') for text in line.split(' -> '))]
    last: Point = None
    for point in points:
        if last:
            if point.x == last.x:
                sign = int(math.copysign(1, point.y - last.y))
                for y in range(last.y, point.y + sign, sign):
                    m[y][point.x] = Field.ROCK
            else:
                sign = int(math.copysign(1, point.x - last.x))
                for x in range(last.x, point.x + sign, sign):
                    m[point.y][x] = Field.ROCK

        last = point

moves = [Point(0, 1), Point(-1, 1), Point(1, 1)]

start_top_left = Point(width, height)
end_bottom_right = Point(0, 0)


def print_map():
    os.system('clear')
    for y in range(start_top_left.y, end_bottom_right.y + 1):
        for x in range(start_top_left.x, end_bottom_right.x + 1):
            if m[y][x] == Field.ROCK:
                print('#', end='')
            elif m[y][x] == Field.SAND:
                print('\033[1;33mo\033[0m', end='')
            else:
                print(' ', end='')
        print()


start = Point(500, 0)

finished = False
count = 0


def check_point(point: Point) -> bool:
    return point.get_value() == Field.EMPTY


while not finished:
    point = start
    turn_finished = False
    while not turn_finished and not finished:
        step_finished = False
        for move in moves:
            if not step_finished:
                new_point = point.add_point(move)

                if new_point.y == height:
                    step_finished = True
                    turn_finished = True
                    finished = True
                    break

                if check_point(new_point):
                    point = new_point
                    step_finished = True

        if not step_finished:
            turn_finished = True

    if not finished:
        count += 1
        m[point.y][point.x] = Field.SAND
        start_top_left = Point(min(point.x - 1, start_top_left.x), min(point.y - 1, start_top_left.y))
        end_bottom_right = Point(max(point.x + 1, end_bottom_right.x), max(point.y + 1, end_bottom_right.y))

    if count > 0:
        print_map()
        time.sleep(0.01)

print_map()

print(count)
