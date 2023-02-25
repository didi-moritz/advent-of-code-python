import re

with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

alpha_pattern = re.compile('[A-Z]')


def count_alphas(line):
    return len(alpha_pattern.findall(line))


def is_alpha(character):
    return alpha_pattern.match(character)


def sum_up(start, end, chars):
    sum = 0
    for i in range(start, end):
        if type(chars[i]) == int:
            sum += chars[i]
        elif is_alpha(chars[i]):
            sum += 1

        chars[i] = ''
    return sum


def calc_line(line):
    chars = list(map(lambda i: i, line))
    for pos in range(len(chars) - 1, -1, -1):
        if chars[pos] == '(':
            end = pos + 1
            while chars[end] != ')':
                end += 1

            end = line.find(')', pos)
            command = line[pos + 1:end]
            length, times = list(map(int, command.split('x')))

            sum = sum_up(pos, end + 1 + length, chars)
            chars[pos] = sum * times

    return sum_up(0, len(chars), chars)


def action():
    for line in data:
        print(line)
        print(calc_line(line))


action()

# X(9x2)(3x3)ABCY
#
# 2 * (3 * 3) = 18 + 2 * 1
#
# XABCABCABCYABCABCABCY
#
# 12
#
# X(3x3)ABC(3x3)ABCY
#
# XABCABCABCABCABCABCY
#
#
# X(10x2)A(2x3)BCZEX
#
# X A(2x3)BCZE A(2x3)BCZE X
# X A BCBCBC ZE A BCBCBC ZE X
# XABCBCBCZEABCBCBCZEX
# -> 20
#
#
# 1 + 2 * (1 + 2 + (2 * 3)) + 1


# X(10x2)A(2x3)BCZEX
# X(10x2)A[6]    ZEX
# X[18]            X
