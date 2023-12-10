import os

with open('day-10.data') as f:
    data = [line.rstrip('\n') for line in f]

dirs = {'|': ((0, -1), (0, 1)),
        '-': ((-1, 0), (1, 0)),
        'L': ((0, -1), (1, 0)),
        'J': ((0, -1), (-1, 0)),
        'F': ((1, 0), (0, 1)),
        '7': ((-1, 0), (0, 1))}

vertical_corners = {'L': -1,
                    'J': -1,
                    'F': 1,
                    '7': 1}

HEIGHT = len(data)
WIDTH = len(data[0])

found = []
nest = []


def print_map():
    os.system('clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            p = (x, y)
            if p in found:
                print(f'\033[96m\033[1m{data[y][x]}\033[0m', end='')
            elif p in nest:
                print(f'\033[31m\033[1m{data[y][x]}\033[0m', end='')
            else:
                print(data[y][x], end='')
        print()


def find_start():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if data[y][x] == 'S':
                return x, y


def find_first(start):
    for d_y in range(-1, 2):
        y = start[1] + d_y
        for d_x in range(-1, 2):
            x = start[0] + d_x
            if 0 <= x < WIDTH and 0 <= y < HEIGHT and (x != 0 or y != 0):
                c = data[y][x]
                if c in dirs:
                    directions = dirs[c]
                    for direction in directions:
                        if direction[0] == -d_x and direction[1] == - d_y:
                            return x, y


def replace_start(start):
    global data

    for c in dirs:
        dir_a, dir_b = dirs[c]
        a = start[0] + dir_a[0], start[1] + dir_a[1]
        b = start[0] + dir_b[0], start[1] + dir_b[1]
        if (a == found[1] and b == found[-1]) or (b == found[1] and a == found[-1]):
            data[start[1]] = data[start[1]].replace('S', c)
            return


def char_open_closes_vertically(c):
    if c in dirs:
        for direction in dirs[c]:
            if direction[1] != 0 and direction[0] == 0:
                return True

    return False


def char_open_closes_corner(c):
    if c in vertical_corners:
        return vertical_corners[c]

    return None


def action():
    global found
    global nest

    start = find_start()
    found.append(start)

    current = find_first(start)
    found.append(current)

    result = 0

    finished = False
    while not finished:
        found_next = False
        for direction in dirs[data[current[1]][current[0]]]:
            new = current[0] + direction[0], current[1] + direction[1]
            if new not in found:
                found_next = True
                current = new
                found.append(current)
                break

        if not found_next:
            finished = True

        result += 1

    replace_start(start)

    for y in range(HEIGHT):
        is_outside = True
        last_corner = None
        for x in range(WIDTH):
            c = data[y][x]
            p = (x, y)

            if p not in found:
                if not is_outside:
                    nest.append(p)

            elif char_open_closes_corner(c):
                new_corner = char_open_closes_corner(c)
                if last_corner:
                    if last_corner == -new_corner:
                        is_outside = not is_outside
                    last_corner = None
                else:
                    last_corner = new_corner

            elif char_open_closes_vertically(c):
                is_outside = not is_outside

    print_map()

    return len(nest)


print(action())
