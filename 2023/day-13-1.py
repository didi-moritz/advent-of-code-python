with open('day-13.data') as f:
    data = [line.rstrip('\n') for line in f]


def print_pattern(pattern):
    for line in pattern:
        print(line)

    print()


def rotate_pattern(pattern):
    new_pattern = []

    for x in range(len(pattern[0])):
        line = ''
        for y in range(len(pattern)):
            line += pattern[y][x]

        new_pattern.append(line)

    return new_pattern


def check_mirror_row(row, pattern):
    height = len(pattern)
    i = 0

    while row - i >= 0 and row + 1 + i < height:
        if pattern[row - i] != pattern[row + i + 1]:
            return False
        i += 1

    return True


def find_mirror_row(pattern):
    for i in range(len(pattern) - 1):
        if check_mirror_row(i, pattern):
            return i + 1

    return None


def action():
    i = 0
    result = 0
    while i < len(data):
        pattern = []
        while i < len(data):
            line = data[i]
            i += 1
            if line == '':
                break
            pattern.append(line)

        mirror_row = find_mirror_row(pattern)
        if mirror_row:
            result += mirror_row * 100
        else:
            pattern = rotate_pattern(pattern)
            mirror_row = find_mirror_row(pattern)
            result += mirror_row

    return result


print(action())

# 97200 too high
