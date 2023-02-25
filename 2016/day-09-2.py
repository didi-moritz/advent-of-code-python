import re

with open('day-09.data') as f:
    data = [line.rstrip('\n') for line in f]

alpha_pattern = re.compile('[A-Z]')


def count_alphas(line):
    return len(alpha_pattern.findall(line))


def calc_range(range_start, range_end, line):
    sum = 0
    pos = range_start
    min_start_pos = -1
    max_end_pos = range_start
    while True:
        s = line.find('(', pos)
        if range_start <= s <= range_end:
            if min_start_pos == -1:
                min_start_pos = s

            e = line.find(')', s)
            if e > 0:
                command = line[s + 1:e]
                length, times = list(map(int, command.split('x')))
                range_sum = calc_range(e + 1, e + length + 1, line)
                sum += range_sum * times

                max_end_pos = max(max_end_pos, e + length + 1)

                pos = e + length + 1
            else:
                break
        else:
            break

    if min_start_pos > -1 and min_start_pos != range_start:
        sum += min_start_pos - range_start

    sum += range_end - max_end_pos

    return sum


result = 0
for line in data:
    print(line)

    number = calc_range(0, len(line), line)
    print(number)

    result += number

print(result)

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
# X(10x2)A(2x3)BCZEX
#
# 1 + 2 * (1 + 2 + (2 * 3)) + 1
