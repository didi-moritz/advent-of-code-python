with open('day-23.data') as f:
    data = [line.rstrip('\n') for line in f]


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'{self.x} × {self.y}'

    def __hash__(self):
        return self.x * 10000 + self.y

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def move(self, point):
        self.x += point.x
        self.y += point.y

    def set(self, point):
        self.x = point.x
        self.y = point.y


class Elf:

    def __init__(self, x, y):
        self.pos = Point(x, y)
        self.move_to = None

    def move_it(self):
        if self.move_to is not None:
            self.pos.set(self.move_to)
            self.move_to = None
            return True
        return False


N = Point(0, -1)
NE = Point(1, -1)
NW = Point(-1, -1)

S = Point(0, 1)
SE = Point(1, 1)
SW = Point(-1, 1)

E = Point(1, 0)
W = Point(-1, 0)

ALL_DIRS = [N, NE, NW, S, SE, SW, E, W]

MOVES = {N: [N, NE, NW], S: [S, SE, SW], W: [W, NW, SW], E: [E, NE, SE]}

moves_order = [N, S, W, E]

elves: list[Elf] = []


def load():
    for y in range(len(data)):
        line = data[y]
        for x in range(len(line)):
            if data[y][x] == '#':
                elves.append(Elf(x, y))


load()


def action():
    global moves_order
    c = 0
    while True:
        c += 1
        if not c % 5:
            print(c)
        occupied = {}
        for elf in elves:
            occupied[elf.pos.__hash__()] = True

        for elf in elves:
            no_need_to_move = True
            for move in ALL_DIRS:
                if elf.pos.add(move).__hash__() in occupied:
                    no_need_to_move = False
                    break

            if no_need_to_move:
                continue

            for move_to in moves_order:
                can_move = True
                for move in MOVES[move_to]:
                    if elf.pos.add(move).__hash__() in occupied:
                        can_move = False
                        break

                if can_move:
                    elf.move_to = elf.pos.add(move_to)
                    break

        for i in range(len(elves)):
            elf = elves[i]
            if elf.move_to is not None:
                collision = False
                for j in range(i + 1, len(elves)):
                    check_elf = elves[j]
                    if check_elf.move_to is not None and elf.move_to == check_elf.move_to:
                        collision = True
                        check_elf.move_to = None
                if collision:
                    elf.move_to = None

        no_move = True
        for elf in elves:
            if elf.move_it():
                no_move = False

        if no_move:
            break

        moves_order = moves_order[1: len(moves_order)] + [moves_order[0]]

    print(c)


action()
