with open('day-18.data') as f:
    data = [line.rstrip('\n') for line in f]


# data = ['1,1,1', '2,1,1']


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


cubes = []

moves = [Cube(1, 0, 0), Cube(-1, 0, 0), Cube(0, 1, 0), Cube(0, -1, 0), Cube(0, 0, 1), Cube(0, 0, -1)]


def read_data():
    for line in data:
        x, y, z = line.split(',')
        cubes.append(Cube(int(x), int(y), int(z)))


read_data()

count = 0

for cube in cubes:
    for move in moves:
        if not cube.add(move) in cubes:
            count += 1

print(count)
