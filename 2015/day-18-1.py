import os
import time

with open('day-18.data') as f:
    data = [line.rstrip('\n') for line in f]

width = len(data[0])
height = len(data)

lights = []


def load():
    for y in range(height):
        lights.append([])
        for x in range(width):
            lights[y].append(data[y][x] == '#')


load()


def get_new_state(x, y):
    count = 0
    for check_y in range(max(0, y - 1), min(height, y + 2)):
        for check_x in range(max(0, x - 1), min(height, x + 2)):
            if x == check_x and y == check_y:
                continue
            if lights[check_y][check_x]:
                count += 1
            if count > 3:
                return False

    if lights[y][x]:
        return 2 <= count <= 3
    else:
        return count == 3


def print_map():
    os.system('clear')
    for y in range(height):
        for x in range(width):
            if lights[y][x]:
                print('\033[96m\033[1m#\033[0m', end='')
            else:
                print(' ', end='')
        print()


count = 0
STEPS = 100


def action():
    global lights
    global count

    for step in range(STEPS):
        new_lights = []
        for y in range(height):
            new_lights.append([])
            for x in range(width):
                new_lights[y].append(get_new_state(x, y))
        lights = new_lights
        print_map()
        print(step)
        time.sleep(0.1)

    for y in range(height):
        for x in range(width):
            if lights[y][x]:
                count += 1


action()

print(count)
