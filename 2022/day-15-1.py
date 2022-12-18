import re

with open('day-15.data') as f:
    data = [line.rstrip('\n') for line in f]

find_row = 2000000

row = {}

line_pattern = re.compile('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
for line in data:
    s_x, s_y, b_x, b_y = [int(i) for i in line_pattern.match(line).groups()]
    d = abs(s_x - b_x) + abs(s_y - b_y)

    d_x = d - abs(s_y - find_row)

    if b_y == find_row:
        row[b_x] = 2

    for x in range(s_x - d_x, s_x + d_x + 1):
        if x not in row:
            row[x] = 1

count = 0
for i in row.keys():
    if row[i] == 1:
        count += 1

print(count)
