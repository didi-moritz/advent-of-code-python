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


def diff_rows(row_a, row_b):
    diff = 0
    for i in range(len(row_a)):
        if row_a[i] != row_b[i]:
            diff += 1

        if diff > 1:
            return 666

    return diff


def check_mirror_row(row, pattern):
    height = len(pattern)
    i = 0

    diff = 0
    while row - i >= 0 and row + 1 + i < height:
        row_a = pattern[row - i]
        row_b = pattern[row + i + 1]
        if row_a != row_b:
            diff += diff_rows(row_a, row_b)

        if diff > 1:
            return False

        i += 1

    return diff == 1


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
