import copy
import os
import sys

sys.setrecursionlimit(10000)

with open('day-24.data') as f:
    data = [line.rstrip('\n') for line in f]

height = len(data)
width = len(data[0])


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x} × {self.y}'

    def __hash__(self):
        return self.x + self.y * width

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def move(self, point):
        self.x += point.x
        self.y += point.y

    def set(self, point):
        self.x = point.x
        self.y = point.y


START = Point(1, 0)
END = Point(width - 2, height - 1)


class Blizzard:

    def __init__(self, pos: Point, move: Point):
        self.pos = pos
        self.move = move

    def move_it(self):
        self.pos.move(self.move)
        if self.pos.x == width - 1:
            self.pos.x = 1
        elif self.pos.x == 0:
            self.pos.x = width - 2
        elif self.pos.y == height - 1:
            self.pos.y = 1
        elif self.pos.y == 0:
            self.pos.y = height - 2


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)
WAIT = Point(0, 0)

ALL_DIRS = [S, E, N, W, WAIT]

start_blizzards: list[Blizzard] = []

start_pos = START


def possible_go_tos(pos):
    return dict(map(lambda m: (pos.add(m), True), ALL_DIRS))


def load():
    for y in range(1, len(data) - 1):
        line = data[y]
        for x in range(1, len(line) - 1):
            if data[y][x] == '.':
                continue

            point = Point(x, y)

            if data[y][x] == '>':
                start_blizzards.append(Blizzard(point, E))
            elif data[y][x] == '<':
                start_blizzards.append(Blizzard(point, W))
            elif data[y][x] == '^':
                start_blizzards.append(Blizzard(point, N))
            else:
                start_blizzards.append(Blizzard(point, S))


load()


def print_map(pos, blizzards, count):
    os.system('clear')
    print(f'count: {count}')
    print(f'best: {min_steps}')
    for y in range(height):
        for x in range(width):
            point = Point(x, y)
            c = '.'

            if point == pos:
                c = '\033[1;32mX\033[0m'
            elif x == 0 or x == width - 1 or y == 0 or y == height - 1 and point != START and point != END:
                c = '#'
            else:
                for blizzard in blizzards:
                    if blizzard.pos == point:
                        if blizzard.move == N:
                            c = '^'
                        elif blizzard.move == S:
                            c = 'v'
                        elif blizzard.move == E:
                            c = '>'
                        else:
                            c = '<'

            print(c, end='')

        print()


min_steps = 100000

iteration = 0


def action(pos: Point, blizzards: list[Blizzard], count: int):
    global min_steps
    global iteration

    if count >= min_steps:
        return

    iteration += 1

    if not iteration % 1000:
        print_map(pos, blizzards, count)

    go_tos = possible_go_tos(pos)

    new_blizzards = copy.deepcopy(blizzards)

    for blizzard in new_blizzards:
        blizzard.move_it()
        if blizzard.pos in go_tos:
            del go_tos[blizzard.pos]

    for go_to in go_tos:
        if go_to == END:
            min_steps = min(min_steps, count)
            break

        if 0 < go_to.x < width - 1 and (0 < go_to.y < height - 1 or go_to == START):
            action(go_to, new_blizzards, count + 1)


action(start_pos, start_blizzards, 1)

print(min_steps)
