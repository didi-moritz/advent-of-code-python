with open('day-01.data') as f:
    data = [line.rstrip('\n') for line in f]


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v, times: int):
        self.x += v.x * times
        self.y += v.y * times

    def length(self):
        return abs(self.x) + abs(self.y)


dirs = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]

dir_i = 0

pos = Vector(0, 0)

commands = data[0].split(', ')

for command in commands:
    rotation = command[0]
    steps = int(command[1:])

    if rotation == 'R':
        dir_i += 1
    else:
        dir_i += -1
    dir_i %= 4

    pos.add(dirs[dir_i], steps)

print(pos.length())
