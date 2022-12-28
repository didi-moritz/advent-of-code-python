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

height = len(data) - 1
width = 0

map = []

pos = Point(0, 0)

moves = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]

commands = []


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

        move = moves[direction]
        inverse_move = moves[(direction + 2) % 4]

        for i in range(steps):
            next = pos.add(move)

            if next.is_outside_or_space():
                while not next.add(inverse_move).is_outside_or_space():
                    next.move(inverse_move)

            if map[next.y][next.x] == BLOCK:
                break

            pos.set(next)

    return (pos.y + 1) * 1000 + (pos.x + 1) * 4 + direction


score = action()

print(score)
