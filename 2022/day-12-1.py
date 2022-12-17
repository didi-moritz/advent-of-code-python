import math
import os
import sys

sys.setrecursionlimit(10000)

with open('day-12.data') as f:
    data = [line.rstrip('\n') for line in f]

width = len(data[0])
height = len(data)

m = []


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

    def get_value(self):
        return m[self.y][self.x]

    def add(self, x, y):
        return Point(self.x + x, self.y + y)

    def add_point(self, point):
        return Point(self.x + point.x, self.y + point.y)


for i in range(height):
    m.append([])

    for j in range(width):
        c = data[i][j]
        if c == 'S':
            start = Point(j, i)
            c = 'a'
        elif c == 'E':
            finish = Point(j, i)
            c = 'z'

        m[i].append(ord(c) - ord('a'))

moves = [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)]


def print_map(points: list[Point]):
    os.system('clear')
    for y in range(height):
        for x in range(width):
            if Point(x, y) in points:
                print('\033[96m\033[1m', end='')
            print(data[y][x], end='')
            print('\033[0m', end='')
        print()


v = {finish: 0}
vv = {finish: [finish]}

max_int = 10000


def jump(point: Point, already: list[Point]):
    new_already = already.copy()
    new_already.append(point)

    min_steps = max_int
    best_new_point = None

    diff_x = finish.x - point.x
    diff_y = finish.y - point.y
    sign_x = int(math.copysign(1, diff_x))
    sign_y = int(math.copysign(1, diff_y))

    new_moves = []

    if abs(diff_x) > abs(diff_y):
        new_moves.append(Point(sign_x, 0))
        new_moves.append(Point(0, sign_y))
        new_moves.append(Point(0, -sign_y))
        new_moves.append(Point(-sign_x, 0))
    else:
        new_moves.append(Point(0, sign_y))
        new_moves.append(Point(sign_x, 0))
        new_moves.append(Point(-sign_x, 0))
        new_moves.append(Point(0, -sign_y))

    for move in new_moves:
        new_point = point.add_point(move)

        if new_point.is_valid() \
                and new_point.get_value() <= (point.get_value() + 1) \
                and new_point not in already \
                and check_surroundings(already, new_point):

            if new_point not in v:
                steps = jump(new_point, new_already) + 1
            else:
                steps = v[new_point] + 1

            if steps < min_steps:
                best_new_point = new_point
                min_steps = steps

    if best_new_point:
        vv[point] = vv[best_new_point].copy()
        vv[point].append(best_new_point)
        v[point] = min_steps
        return min_steps
    else:
        v[point] = max_int
        return max_int


def check_surroundings(already, new_point):
    for move in moves:
        check_point = new_point.add_point(move)
        if check_point in already and (check_point.get_value() >= (new_point.get_value() - 1)):
            return False

    return True


jump(start, [])

for y in range(height):
    for x in range(width):
        point = Point(x, y)
        if point not in vv[start] and point != start:
            if point in v:
                del v[point]
            if point in vv:
                del vv[point]

jump(start, [])

all_steps = vv[start].copy()
all_steps.append(start)
print_map(all_steps)

print('finished')
print(v[start])
