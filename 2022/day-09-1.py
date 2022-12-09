with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

dots = [[False for i in range(1000)] for j in range(1000)]


class Point:
    x = 500
    y = 500


h = Point()
t = Point()

for line in data:
    direction = line.split(' ')[0]
    steps = int(line.split(' ')[1])

    for i in range(steps):
        if direction == 'D':
            h.y += 1
        elif direction == 'U':
            h.y -= 1
        elif direction == 'R':
            h.x += 1
        else:
            h.x -= 1

        diff_x = abs(h.x - t.x)
        diff_y = abs(h.y - t.y)
        move_diagonally = (diff_x + diff_y) > 2

        if diff_x > 1:
            t.x = int((t.x + h.x) / 2)
            if move_diagonally:
                t.y = h.y

        if diff_y > 1:
            t.y = int((t.y + h.y) / 2)
            if move_diagonally:
                t.x = h.x

        dots[t.y][t.x] = True

score = 0
for dots_line in dots:
    for dot in dots_line:
        if dot:
            score += 1

print(score)
