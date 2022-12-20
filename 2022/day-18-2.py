import sys

with open('day-18.data') as f:
    data = [line.rstrip('\n') for line in f]

sys.setrecursionlimit(10000)


class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}x{self.y}x{self.z}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return self.x * 1000 + self.y * 100 + self.z

    def add(self, other):
        return Cube(self.x + other.x, self.y + other.y, self.z + other.z)


cubes: list[Cube] = []


def read_data():
    for line in data:
        x, y, z = line.split(',')
        cubes.append(Cube(int(x), int(y), int(z)))


read_data()

outside = []
moves = [Cube(1, 0, 0), Cube(-1, 0, 0), Cube(0, 1, 0), Cube(0, -1, 0), Cube(0, 0, 1), Cube(0, 0, -1)]

min_x = 100
min_y = 100
min_z = 100
max_x = 0
max_y = 0
max_z = 0


def find_outside_cube(cube: Cube):
    if min_x <= cube.x <= max_x and min_y <= cube.y <= max_y and min_z <= cube.z <= max_z \
            and cube not in outside \
            and cube not in cubes:
        outside.append(cube)
        for move in moves:
            find_outside_cube(cube.add(move))


def find_outside():
    global min_x, min_y, min_z, max_x, max_y, max_z
    for cube in cubes:
        min_x = min(min_x, cube.x - 1)
        min_y = min(min_y, cube.y - 1)
        min_z = min(min_z, cube.z - 1)
        max_x = max(max_x, cube.x + 1)
        max_y = max(max_y, cube.y + 1)
        max_z = max(max_z, cube.z + 1)

    find_outside_cube(Cube(min_x, min_y, min_z))
    print('found outside')


find_outside()


def action():
    count = 0

    for cube in cubes:
        for move in moves:
            if cube.add(move) in outside:
                count += 1
    print(count)


action()
