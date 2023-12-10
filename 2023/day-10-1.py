import os
import time

with open('day-10.data') as f:
    data = [line.rstrip('\n') for line in f]

dirs = {'|': ((0, -1), (0, 1)),
        '-': ((-1, 0), (1, 0)),
        'L': ((0, -1), (1, 0)),
        'J': ((0, -1), (-1, 0)),
        'F': ((1, 0), (0, 1)),
        '7': ((-1, 0), (0, 1))}

HEIGHT = len(data)
WIDTH = len(data[0])

found = []


def print_map():
    os.system('clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in found:
                print(f'\033[96m\033[1m{data[y][x]}\033[0m', end='')
            else:
                print(data[y][x], end='')
        print()


def find_start():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if data[y][x] == 'S':
                return tuple((x, y))


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
                            return tuple((x, y))


def action():
    global found

    start = find_start()
    found.append(start)

    current = find_first(start)
    found.append(current)

    result = 0

    finished = False
    while not finished:
        found_next = False
        for direction in dirs[data[current[1]][current[0]]]:
            new = tuple((current[0] + direction[0], current[1] + direction[1]))
            if new not in found:
                found_next = True
                current = new
                found.append(current)
                break

        if not found_next:
            finished = True

        result += 1
        if result % 200 == 0:
            print_map()
            time.sleep(0.3)

    print_map()
    return int((result + 1) / 2)


print(action())

# 2416390430 too high
