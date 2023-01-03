import math

with open('day-25.data') as f:
    data = [line.rstrip('\n') for line in f]

# convert = {'=': 0, '-': 1, '0': 2, '1': 3, '2': 4}
# inverse_convert = {0: '=', 1: '-', 2: '0', 3: '1', 4: '2'}
convert = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
inverse_convert = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}


def toDecimal(line):
    n = 0
    for i in range(len(line)):
        c = line[len(line) - i - 1]
        n += convert[c] * int(math.pow(5, i))
    return n


def toSnafu(number):
    result = ''
    for i in range(32, -1, -1):
        f = int(math.pow(5, i))
        d = math.ceil(f / 2) - 1
        r = 0
        if number < - d:
            if number < - f - d:
                r = -2
            else:
                r = -1
        elif number > d:
            if number > f + d:
                r = 2
            else:
                r = 1

        number -= r * f

        if len(result) > 0 or r != 0:
            result = result + inverse_convert[r]
    return result


total = 0
for line in data:
    decimal = toDecimal(line)
    snafu = toSnafu(decimal)
    print(f'{line} -> {decimal} -> {snafu}')
    total += decimal

print(toSnafu(total))
