import copy
import os
import time

with open('day-17.data') as f:
    data = [line.rstrip('\n') for line in f]

jets = data[0]

brick_data = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x} × {self.y}'

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def move(self, point):
        self.x += point.x
        self.y += point.y


class Brick:
    def __init__(self, points: list[Point], color: int):
        self.points = points
        self.color = color

    def move(self, move: Point):
        for point in self.points:
            point.move(move)

    def can_move(self, move: Point):
        for point in self.points:
            check = point.add(move)
            if (width <= check.x or check.x < 0 or m[check.y][check.x] != 0) or check.y < 0:
                return False

        return True

    def fix(self):
        for point in self.points:
            m[point.y][point.x] = self.color


width = 7
max_height = 10000

m = []
for i in range(max_height):
    m.append([0] * width)

bricks: list[Brick] = []


def load_bricks():
    color = 31
    for brick_block in brick_data.strip('\n').split('\n\n'):
        points = []
        lines = brick_block.split('\n')
        for y in range(len(lines)):
            line = lines[-y - 1]
            for x in range(len(line)):
                if line[x] == '#':
                    points.append(Point(x, y))
        bricks.append(Brick(points, color))
        color += 1


load_bricks()


def current_height():
    for y in range(max_height):
        empty = True
        for x in range(width):
            if m[y][x] != 0:
                empty = False
                break
        if empty:
            return y
    return 0


def print_map():
    os.system('clear')
    y_to = current_height()
    for y in range(y_to, max(-2, y_to - 51), -1):
        for x in range(-1, width + 1):
            if x < 0 or x == width or y == -1:
                print('%', end='')
            elif m[y][x] > 0:
                print(f'\033[{m[y][x]}m\033[1m#\033[0m', end='')
            else:
                print(' ', end='')
        print()


move_left = Point(-1, 0)
move_right = Point(1, 0)
move_down = Point(0, -1)


def action():
    brick_i = 0
    jets_i = 0
    for i in range(2022):
        brick = copy.deepcopy(bricks[brick_i])
        brick.move(Point(2, current_height() + 3))

        while True:
            move_jet = move_right if jets[jets_i] == '>' else move_left
            if brick.can_move(move_jet):
                brick.move(move_jet)
            jets_i = (jets_i + 1) % len(jets)

            if brick.can_move(move_down):
                brick.move(move_down)
            else:
                brick.fix()
                break

        brick_i = (brick_i + 1) % len(bricks)

        if i > 1900:
            print_map()
            print(i)
            time.sleep(0.03)


action()

print(current_height())
