with open('day-11.data') as f:
    data = [line.rstrip('\n') for line in f]


class P:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def expand_horizontally(galaxy):
    for x in range(len(galaxy[0]) - 1, -1, -1):
        is_empty = True
        for y in range(len(galaxy)):
            if galaxy[y][x] != '.':
                is_empty = False
                break

        if is_empty:
            for y in range(len(galaxy)):
                galaxy[y] = galaxy[y][:x] + '.' + galaxy[y][x:]

    return galaxy


def expand_vertically(galaxy):
    new_galaxy = []
    for y in range(len(galaxy)):
        is_empty = True
        for x in range(len(galaxy[y])):
            if galaxy[y][x] != '.':
                is_empty = False
                break

        new_galaxy.append(galaxy[y])
        if is_empty:
            new_galaxy.append(galaxy[y])

    return new_galaxy


def find_stars(galaxy):
    stars: list[P] = []
    for y in range(len(galaxy)):
        for x in range(len(galaxy[y])):
            if galaxy[y][x] == '#':
                stars.append(P(x, y))

    return stars


def action():
    galaxy = expand_horizontally(data)
    galaxy = expand_vertically(galaxy)

    stars = find_stars(galaxy)

    result = 0
    for i in range(len(stars)):
        s1 = stars[i]
        for j in range(i, len(stars)):
            s2 = stars[j]
            result += abs(s1.x - s2.x) + abs(s1.y - s2.y)

    return result


print(action())
