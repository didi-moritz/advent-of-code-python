import math

with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

dots = [[False for i in range(1000)] for j in range(1000)]


class Point:
    x = 500
    y = 500


knots = [Point() for i in range(10)]

for line in data:
    direction = line.split(' ')[0]
    steps = int(line.split(' ')[1])

    for i in range(steps):
        if direction == 'D':
            knots[0].y += 1
        elif direction == 'U':
            knots[0].y -= 1
        elif direction == 'R':
            knots[0].x += 1
        else:
            knots[0].x -= 1

        for j in range(1, len(knots)):
            h = knots[j - 1]
            t = knots[j]
            while True:
                diff_x = h.x - t.x
                diff_y = h.y - t.y

                if abs(diff_x) > 1:
                    t.x += int(math.copysign(1, diff_x))
                    if diff_y != 0:
                        t.y += int(math.copysign(1, diff_y))

                elif abs(diff_y) > 1:
                    t.y += int(math.copysign(1, diff_y))
                    if diff_x != 0:
                        t.x += int(math.copysign(1, diff_x))

                if j == len(knots) - 1:
                    dots[t.y][t.x] = True

                if diff_x < 2 and diff_y < 2:
                    break

score = 0
for dots_line in dots:
    for dot in dots_line:
        print('x' if dot else ' ', end='')
        if dot:
            score += 1
    print()

print(score)
