with open('day-02.data') as f:
    data = [line.rstrip('\n') for line in f]

pad = [
    '  1',
    ' 234',
    '56789',
    ' ABC',
    '  D']

m = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}


def action():
    x = 0
    y = 2

    result = ''

    for line in data:
        for c in line:
            new_x = x + m[c][0]
            new_y = y + m[c][1]

            if 0 <= new_y < len(pad) and 0 <= new_x < len(pad[new_y]) and pad[new_y][new_x] != ' ':
                x = new_x
                y = new_y

        result = f'{result}{pad[y][x]}'

    return result


print(action())
