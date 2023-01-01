import copy
import os
import sys

sys.setrecursionlimit(10000)

with open('day-24.data') as f:
    data = [line.rstrip('\n') for line in f]

height = len(data) - 2
width = len(data[0]) - 2


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


START = Point(0, -1)
END = Point(width - 1, height)


class Blizzard:

    def __init__(self, pos: Point, move: Point):
        self.pos = pos
        self.move = move

    def get_pos(self, minute):
        point = self.pos.add(Point(self.move.x * minute, self.move.y * minute))
        point.set(Point(point.x % width, point.y % height))
        return point


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)
WAIT = Point(0, 0)

ALL_DIRS = [S, E, N, W, WAIT]

blizzards_h = {}
blizzards_v = {}
blizzards_all = []
already_visited = {}

start_pos = START


def possible_go_tos(pos):
    return dict(map(lambda m: (pos.add(m), True), ALL_DIRS))


def load():
    for y in range(height):
        blizzards_h[y] = []
    for x in range(width):
        blizzards_v[x] = []

    for y in range(height):
        for x in range(width):
            if data[y + 1][x + 1] == '.':
                continue

            point = Point(x, y)

            if data[y + 1][x + 1] == '>':
                blizzards_h[y].append(Blizzard(point, E))
            elif data[y + 1][x + 1] == '<':
                blizzards_h[y].append(Blizzard(point, W))
            elif data[y + 1][x + 1] == '^':
                blizzards_v[x].append(Blizzard(point, N))
            else:
                blizzards_v[x].append(Blizzard(point, S))

    for blizzards in blizzards_v.values():
        for blizzard in blizzards:
            blizzards_all.append(blizzard)

    for blizzards in blizzards_h.values():
        for blizzard in blizzards:
            blizzards_all.append(blizzard)


load()


def print_map(pos, minute):
    os.system('clear')
    print(f'minute: {minute}')
    print(f'best: {min_steps}')

    m = []
    for y in range(height):
        m.append([])
        for x in range(width):
            m[y].append(' ')

    for blizzard in blizzards_all:
        point = blizzard.get_pos(minute)
        if blizzard.move == N:
            c = '^'
        elif blizzard.move == S:
            c = 'v'
        elif blizzard.move == E:
            c = '>'
        else:
            c = '<'
        m[point.y][point.x] = c

    for y in range(-1, height + 1):
        for x in range(-1, width + 1):
            point = Point(x, y)

            if point == pos:
                c = '\033[1;32mX\033[0m'
            elif point == START or point == END:
                c = ' '
            elif x == -1 or x == width or y == -1 or y == height:
                c = '#'
            else:
                c = m[y][x]

            print(c, end='')

        print()


min_steps = 100000

iteration = 0


def action(pos: Point, minute: int):
    global min_steps
    global iteration

    if minute >= min_steps:
        return

    if pos in already_visited:
        if minute in already_visited[pos]:
            return
    else:
        already_visited[pos] = []

    already_visited[pos].append(minute)

    iteration += 1

    if not iteration % 10000:
        print_map(pos, minute)

    go_tos = possible_go_tos(pos)

    min_x = width
    max_x = 0
    min_y = height
    max_y = 0

    go_to_keys = copy.deepcopy(list(go_tos.keys()))
    for go_to in go_to_keys:
        if go_to == END:
            min_steps = min(min_steps, minute)
            return

        if (0 > go_to.x or go_to.x >= width) or (0 > go_to.y or go_to.y >= height) and go_to != START:
            del go_tos[go_to]

    for go_to in go_tos:
        min_x = min(min_x, go_to.x)
        max_x = max(max_x, go_to.x)
        min_y = min(min_y, go_to.y)
        max_y = max(max_y, go_to.y)

    for y in range(min_y, max_y + 1):
        if 0 <= y < height:
            for blizzard in blizzards_h[y]:
                point = blizzard.get_pos(minute)
                if point in go_tos:
                    del go_tos[point]

    for x in range(min_x, max_x + 1):
        if 0 <= x < width:
            for blizzard in blizzards_v[x]:
                point = blizzard.get_pos(minute)
                if point in go_tos:
                    del go_tos[point]

    for go_to in go_tos:
        if go_to == END:
            min_steps = min(min_steps, minute)
            break

        action(go_to, minute + 1)


action(start_pos, 1)

print(min_steps)
