import math

with open('day-11.data') as f:
    data = [line.rstrip('\n') for line in f]


class P:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def find_empty_columns(galaxy):
    cols = []
    for x in range(len(galaxy[0]) - 1, -1, -1):
        is_empty = True
        for y in range(len(galaxy)):
            if galaxy[y][x] != '.':
                is_empty = False
                break

        if is_empty:
            cols.append(x)

    return cols


def find_empty_rows(galaxy):
    rows = []
    for y in range(len(galaxy)):
        is_empty = True
        for x in range(len(galaxy[y])):
            if galaxy[y][x] != '.':
                is_empty = False
                break

        if is_empty:
            rows.append(y)

    return rows


def find_stars(galaxy):
    stars: list[P] = []
    for y in range(len(galaxy)):
        for x in range(len(galaxy[y])):
            if galaxy[y][x] == '#':
                stars.append(P(x, y))

    return stars


def action():
    galaxy = data
    stars = find_stars(galaxy)

    cols = find_empty_columns(galaxy)
    rows = find_empty_rows(galaxy)

    result = 0
    for i in range(len(stars)):
        s1 = stars[i]
        for j in range(i, len(stars)):
            s2 = stars[j]
            result += abs(s1.x - s2.x) + abs(s1.y - s2.y)
            for row in rows:
                if int(math.copysign(1, s1.y - row)) != int(math.copysign(1, s2.y - row)):
                    result += 1000000 - 1
            for col in cols:
                if int(math.copysign(1, s1.x - col)) != int(math.copysign(1, s2.x - col)):
                    result += 1000000 - 1

    return result


print(action())
