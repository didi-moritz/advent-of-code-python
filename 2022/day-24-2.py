import os
import sys

sys.setrecursionlimit(20000)

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
INVALID = Point(- 1, -1)


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

ALL_DIRS_1_3 = [S, E, N, W, WAIT]

ALL_DIRS_2 = [W, N, E, S, WAIT]

blizzards_h = []
blizzards_v = []
blizzards_all = []
already_visited = {}


def possible_go_tos(pos, way):
    return dict(map(lambda m: (pos.add(m), True), ALL_DIRS_2 if way == 2 else ALL_DIRS_1_3))


def load():
    for y in range(height):
        for x in range(width):
            if data[y + 1][x + 1] == '.':
                continue

            point = Point(x, y)

            if data[y + 1][x + 1] == '>':
                blizzards_h.append(Blizzard(point, E))
            elif data[y + 1][x + 1] == '<':
                blizzards_h.append(Blizzard(point, W))
            elif data[y + 1][x + 1] == '^':
                blizzards_v.append(Blizzard(point, N))
            else:
                blizzards_v.append(Blizzard(point, S))

    for blizzard in blizzards_v:
        blizzards_all.append(blizzard)

    for blizzard in blizzards_h:
        blizzards_all.append(blizzard)


load()

blizzards_h_map = []
blizzards_v_map = []


def create_empty_map():
    m = []
    for y in range(height):
        m.append([False] * width)
    return m


def fill_maps():
    for minute in range(height):
        m = create_empty_map()

        for blizzard in blizzards_v:
            point = blizzard.get_pos(minute)
            m[point.y][point.x] = True

        blizzards_v_map.append(m)

    for minute in range(width):
        m = create_empty_map()

        for blizzard in blizzards_h:
            point = blizzard.get_pos(minute)
            m[point.y][point.x] = True

        blizzards_h_map.append(m)


fill_maps()


def print_map(pos, minute, way):
    os.system('clear')
    print(f'way: #{way}, minute: {minute}')
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


def action(pos: Point, finish: Point, minute: int, way: int):
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
        print_map(pos, minute, way)

    go_tos = possible_go_tos(pos, way)

    for go_to in go_tos:
        if go_to == finish:
            min_steps = min(min_steps, minute)
            return

        if go_to == START or go_to == END:
            continue

        if (0 > go_to.x or go_to.x >= width) or (0 > go_to.y or go_to.y >= height):
            go_tos[go_to] = False
        elif blizzards_v_map[minute % height][go_to.y][go_to.x]:
            go_tos[go_to] = False
        elif blizzards_h_map[minute % width][go_to.y][go_to.x]:
            go_tos[go_to] = False

    for go_to in go_tos:
        if go_tos[go_to]:
            action(go_to, finish, minute + 1, way)


action(START, END, 1, 1)
print(min_steps)
min_steps_1 = min_steps
min_steps = 100000
already_visited = {}

action(END, START, min_steps_1 + 1, 2)
print(min_steps)
min_steps_2 = min_steps
min_steps = 100000
already_visited = {}

action(START, END, min_steps_2 + 1, 3)

print(min_steps)
