import re

with open('day-15.data') as f:
    data = [line.rstrip('\n') for line in f]

max_x_y = 4000000

senders = []

line_pattern = re.compile('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
for line in data:
    s_x, s_y, b_x, b_y = [int(i) for i in line_pattern.match(line).groups()]
    d = abs(s_x - b_x) + abs(s_y - b_y)

    senders.append([s_x, s_y, d])


def check_point(x, y):
    if x < 0 or x > max_x_y or y < 0 or y > max_x_y:
        return

    for sender in senders:
        if abs(sender[0] - x) + abs(sender[1] - y) <= sender[2]:
            return

    print(f'{x} × {y} -> {x * max_x_y + y}')
    exit(1)


def check():
    for sender in senders:
        d = sender[2] + 1
        for d_x in range(-d, d + 1):
            d_y = d - d_x
            check_point(sender[0] + d_x, sender[1] + d_y)
            check_point(sender[0] + d_x, sender[1] - d_y)

    print('finished one sender')


check()
