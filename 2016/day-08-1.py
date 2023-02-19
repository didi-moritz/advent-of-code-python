import os
import re
import time

with open('day-08.data') as f:
    data = [line.rstrip('\n') for line in f]

rect_pattern = re.compile(r"^rect (\d+)x(\d+)$")
rotate_row_pattern = re.compile(r"^rotate row y=(\d+) by (\d+)$")
rotate_column_pattern = re.compile(r"^rotate column x=(\d+) by (\d+)$")

WIDTH = 50
HEIGHT = 6

lcd = [[False] * WIDTH for y in range(HEIGHT)]


def print_lcd():
    os.system('clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print('#' if lcd[y][x] else ' ', end='')
        print()


for line in data:
    if rect_pattern.match(line):
        width, height = list(map(int, rect_pattern.match(line).groups()))
        for y in range(height):
            for x in range(width):
                lcd[y][x] = True
    elif rotate_row_pattern.match(line):
        y, step = list(map(int, rotate_row_pattern.match(line).groups()))
        for i in range(step):
            lcd[y].insert(0, lcd[y].pop())
    elif rotate_column_pattern.match(line):
        x, step = list(map(int, rotate_column_pattern.match(line).groups()))
        for i in range(step):
            last = lcd[HEIGHT - 1][x]
            for y in range(HEIGHT - 1, 0, -1):
                lcd[y][x] = lcd[y - 1][x]
            lcd[0][x] = last

    print_lcd()
    time.sleep(0.2)

result = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if lcd[y][x]:
            result += 1

print(result)
