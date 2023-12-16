with open('day-16.data') as f:
    data = [line.rstrip('\n') for line in f]

HEIGHT = len(data)
WIDTH = len(data[0])


class P:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x + self.y * WIDTH)

    def __eq__(self, other):
        return self.x == other.x and self.x == other.y


class Beam:
    def __init__(self, pos: P, vect: P):
        self.pos = pos
        self.vect = vect


beams = []
visited = {}


def check_visited(beam: Beam):
    hash_pos = hash(beam.pos)
    return hash_pos in visited and hash(beam.vect) in visited[hash_pos]


def add_visited(beam: Beam):
    hash_pos = hash(beam.pos)
    if hash_pos not in visited:
        visited[hash_pos] = []

    hash_vect = hash(beam.vect)
    visited[hash_pos].append(hash_vect)


def move_beam(beam: Beam):
    global beams

    while True:
        if beam.pos.x < 0 or beam.pos.x >= WIDTH or beam.pos.y < 0 or beam.pos.y >= HEIGHT:
            return

        if check_visited(beam):
            return

        add_visited(beam)

        c = data[beam.pos.y][beam.pos.x]

        if c == '/':
            if beam.vect.y == 0:
                beam.vect = P(0, -beam.vect.x)
            else:
                beam.vect = P(-beam.vect.y, 0)
        elif c == '\\':
            if beam.vect.y == 0:
                beam.vect = P(0, beam.vect.x)
            else:
                beam.vect = P(beam.vect.y, 0)
        elif c == '|':
            if beam.vect.y == 0:
                beam.vect = P(0, 1)
                beams.append(Beam(beam.pos, P(0, -1)))
        elif c == '-':
            if beam.vect.x == 0:
                beam.vect = P(1, 0)
                beams.append(Beam(beam.pos, P(-1, 0)))

        beam.pos = P(beam.pos.x + beam.vect.x, beam.pos.y + beam.vect.y)


def action():
    global beams

    beams.append(Beam(P(0, 0), P(1, 0)))

    while beams:
        move_beam(beams.pop())

    return len(visited)


print(action())
