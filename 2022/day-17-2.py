import copy
import time

start = time.time()

with open('day-17.data') as f:
    data = [line.rstrip('\n') for line in f]

jets = []
for d in data[0]:
    jets.append(-1 if d == '<' else 1)

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
        length = 0
        for point in points:
            length = max(length, point.x + 1)
        self.length = length

    def move(self, move: Point):
        for point in self.points:
            point.move(move)

    def can_move(self, move: Point):
        for point in self.points:
            check = point.add(move)
            if (width <= check.x or check.x < 0 or m[check.y][check.x] != 0) or check.y < 0:
                return False

        return True

    def get_height(self):
        h = 0
        for point in self.points:
            h = max(h, point.y)
        return h

    def fix(self):
        for point in self.points:
            m[point.y][point.x] = self.color


width = 7
max_height = 1000000

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

move_left = Point(-1, 0)
move_right = Point(1, 0)
move_down = Point(0, -1)

STOP = 1000000000000


def action():
    bricks_i = 0
    jets_i = 0
    height = 0
    height_offset = 0

    jets_break_i = -1
    first_jets_round_i = 0
    first_jets_round_bricks_i = 0
    first_jets_round_height = 0

    i = 0
    while i < STOP:
        brick = copy.deepcopy(bricks[bricks_i])

        x = 2
        for j in range(3):
            x = min(max(0, x + jets[jets_i]), width - brick.length)
            jets_i = (jets_i + 1) % len(jets)

        brick.move(Point(x, height))

        while True:
            move_jet = move_right if jets[jets_i] == 1 else move_left
            if brick.can_move(move_jet):
                brick.move(move_jet)
            jets_i = (jets_i + 1) % len(jets)

            if brick.can_move(move_down):
                brick.move(move_down)
            else:
                brick.fix()
                height = max(height, brick.get_height() + 1)
                break

        if i > 100 and jets_break_i == -1:
            jets_break_i = jets_i

        if jets_i == jets_break_i:
            if not first_jets_round_i:
                first_jets_round_i = i
                first_jets_round_height = height
                first_jets_round_bricks_i = bricks_i
                print(f'first_jets_round_i: {first_jets_round_i}')
                print(f'first_jets_round_height: {first_jets_round_height}')
            elif not height_offset and bricks_i == first_jets_round_bricks_i:
                print(f'second_jets_round_i: {i}')
                print(f'second_jets_round_height: {height}')
                print(f'second_jets_round_bricks_i: {bricks_i}')
                d_i = i - first_jets_round_i
                d_height = height - first_jets_round_height
                print(f'd_i: {d_i}')
                print(f'd_height: {d_height}')

                jumps = int((STOP - i) / d_i)
                print(f'jumps: {jumps}')

                height_offset = d_height * jumps
                i += d_i * jumps

        bricks_i = (bricks_i + 1) % len(bricks)
        i += 1

    return height + height_offset


print(f'result: {action()}')

end = time.time()

print(f'duration: {(end - start) * 1000}ms')
