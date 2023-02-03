with open('day-01.data') as f:
    data = [line.rstrip('\n') for line in f]


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def __hash__(self):
        return self.x * 10000 + self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def length(self):
        return abs(self.x) + abs(self.y)

    def clone(self):
        return Vector(self.x, self.y)


dirs = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]

pos = Vector(0, 0)

commands = data[0].split(', ')

visited = {pos.clone()}


def action():
    dir_i = 0
    for command in commands:
        rotation = command[0]
        steps = int(command[1:])

        if rotation == 'R':
            dir_i += 1
        else:
            dir_i += -1
        dir_i %= 4

        for i in range(steps):
            pos.add(dirs[dir_i])

            if pos in visited:
                return

            visited.add(pos.clone())


action()

print(pos.length())
