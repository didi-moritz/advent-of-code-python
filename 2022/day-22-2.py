with open('day-22.data') as f:
    data = [line.rstrip('\n') for line in f]


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

    def is_outside(self):
        return self.x < 0 or self.y < 0 or self.x >= width or self.y >= height

    def get_type(self):
        return OUTSIDE if self.is_outside() else map[self.y][self.x]

    def is_outside_or_space(self):
        return self.get_type() in [OUTSIDE, SPACE]

    def set(self, point):
        self.x = point.x
        self.y = point.y


SPACE = 0
EMPTY = 1
BLOCK = 2
OUTSIDE = 4

height = len(data) - 2
width = 0

map = []

pos = Point(0, 0)

moves = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]

commands = []


def warp(next_pos):
    # 1 -> 6
    if next_pos.y == -1 and 50 <= next_pos.x < 100:
        next_pos.set(Point(0, 150 + next_pos.x - 50))
        return 0

    # 2 -> 6
    if next_pos.y == -1 and 100 <= next_pos.x:
        next_pos.set(Point(next_pos.x - 100, height - 1))
        return 3

    # 2 -> 5
    if next_pos.x == width and next_pos.y < 50:
        next_pos.set(Point(99, 100 + 49 - next_pos.y))
        return 2

    # 2 -> 3
    if next_pos.y == 50 and 100 <= next_pos.x:
        next_pos.set(Point(99, 50 + next_pos.x - 100))
        return 2

    # 3 -> 2
    if next_pos.x == 100 and 50 <= next_pos.y < 100:
        next_pos.set(Point(100 + next_pos.y - 50, 49))
        return 3

    # 5 -> 2
    if next_pos.x == 100 and 100 <= next_pos.y:
        next_pos.set(Point(149, 149 - next_pos.y))
        return 2

    # 5 -> 6
    if next_pos.y == 150 and 50 <= next_pos.x:
        next_pos.set(Point(49, 150 + next_pos.x - 50))
        return 2

    # 6 -> 5
    if next_pos.x == 50 and 150 <= next_pos.y:
        next_pos.set(Point(50 + next_pos.y - 150, 149))
        return 3

    # 6 -> 2
    if next_pos.y == height and next_pos.x < 50:
        next_pos.set(Point(100 + next_pos.x, 0))
        return 1

    # 6 -> 1
    if next_pos.x == -1 and 150 <= next_pos.y:
        next_pos.set(Point(50 + next_pos.y - 150, 0))
        return 1

    # 4 -> 1
    if next_pos.x == -1 and 100 <= next_pos.y < 150:
        next_pos.set(Point(50, 149 - next_pos.y))
        return 0

    # 4 -> 3
    if next_pos.y == 99 and next_pos.x < 50:
        next_pos.set(Point(50, 50 + next_pos.x))
        return 0

    # 3 -> 4
    if next_pos.x == 49 and 50 <= next_pos.y < 100:
        next_pos.set(Point(next_pos.y - 50, 100))
        return 1

    # 1 -> 4
    if next_pos.x == 49 and next_pos.y < 50:
        next_pos.set(Point(0, 100 + 49 - next_pos.y))
        return 0

    #      49  99
    #     0 |50|100
    #     | || || |149
    # +------+    +---+
    # | +----111222   |    0
    # | |    111222   |
    # | |    111222-+ |    49
    # | | +--333  | | |    50
    # | | |  333  | | |
    # | | |  333--+ | |    99
    # | | 444555----+ |    100
    # | | 444555      |
    # | +-444555      |    149
    # +---666 |       |    150
    #     666-+       |
    #     666         |    199
    #       +---------+
    #     0 45 91 1
    #       90 90 4
    #           0 9


def load_and_init():
    global width
    for y in range(0, height):
        width = max(width, len(data[y]))

    for y in range(0, height):
        map.append([])
        for x in range(0, width):
            type = SPACE
            if x < len(data[y]) and data[y][x] != ' ':
                type = BLOCK if data[y][x] == '#' else EMPTY

            map[y].append(type)

    for x in range(0, width):
        if map[0][x] == EMPTY:
            pos.move(Point(x, 0))
            break

    line = data[len(data) - 1]

    l_splits = line.split('L')

    for i in range(0, len(l_splits)):
        r_splits = l_splits[i].split('R')

        for j in range(0, len(r_splits)):
            commands.append(r_splits[j])

            if j != len(r_splits) - 1:
                commands.append('R')

        if i != len(l_splits) - 1:
            commands.append('L')


load_and_init()


def action():
    direction = 0
    for command in commands:
        if command == 'R' or command == 'L':
            direction += 1 if command == 'R' else -1
            direction %= 4
            continue

        steps = int(command)

        for i in range(steps):
            move = moves[direction]
            new_direction = None
            next_pos = pos.add(move)

            if next_pos.is_outside_or_space():
                new_direction = warp(next_pos)

            if map[next_pos.y][next_pos.x] == BLOCK:
                break

            if new_direction is not None:
                direction = new_direction

            pos.set(next_pos)

    return (pos.y + 1) * 1000 + (pos.x + 1) * 4 + direction


score = action()

print(score)
