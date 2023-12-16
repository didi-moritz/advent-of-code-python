import time

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


def check_visited(beam: Beam, visited):
    hash_pos = hash(beam.pos)
    return hash_pos in visited and hash(beam.vect) in visited[hash_pos]


def add_visited(beam: Beam, visited):
    hash_pos = hash(beam.pos)
    if hash_pos not in visited:
        visited[hash_pos] = []

    hash_vect = hash(beam.vect)
    visited[hash_pos].append(hash_vect)


def move_beam(beam: Beam, beams, visited):
    while True:
        if beam.pos.x < 0 or beam.pos.x >= WIDTH or beam.pos.y < 0 or beam.pos.y >= HEIGHT:
            return beams

        if check_visited(beam, visited):
            return beams

        add_visited(beam, visited)

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


def run(pos, vect):
    beams = []
    visited = {}

    beams.append(Beam(pos, vect))

    while beams:
        beams = move_beam(beams.pop(), beams, visited)

    return len(visited)


def action():
    result = 0

    for y in range(HEIGHT):
        result = max(result, run(P(0, y), P(1, 0)))
        result = max(result, run(P(WIDTH - 1, y), P(-1, 0)))

    for x in range(WIDTH):
        result = max(result, run(P(x, 0), P(0, 1)))
        result = max(result, run(P(x, HEIGHT - 1), P(0, -1)))

    return result


start = time.time()
print(action())
end = time.time()
print(f'{end - start}')
