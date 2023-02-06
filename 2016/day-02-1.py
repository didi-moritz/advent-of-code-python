import os
import time

with open('day-02.data') as f:
    data = [line.rstrip('\n') for line in f]


def print_sep_line():
    print('+---+---+---+')


def print_pad(current: int, code):
    os.system('clear')

    print_sep_line()
    for y in range(3):
        print('|', end='')
        for x in range(3):
            number = (x + 1) + 3 * y
            if current == number:
                print(f' \033[96m\033[1m{number}\033[0m ', end='')
            else:
                print(f' {number} ', end='')
            print('|', end='')
        print()
        print_sep_line()
    print()
    print()
    print(code)


def action():
    pos = 5

    result = ''

    for line in data:
        for c in line:
            if c == 'U':
                new_pos = pos - 3
            elif c == 'L':
                if pos != 4 and pos != 7:
                    new_pos = pos - 1
            elif c == 'D':
                new_pos = pos + 3
            elif c == 'R':
                if pos != 3 and pos != 6:
                    new_pos = pos + 1

            if 1 <= new_pos <= 9:
                pos = new_pos

            # print_pad(pos, result)
            # time.sleep(0.0001)

        result = f'{result}{pos}'

        print_pad(pos, result)
        time.sleep(0.1)

    print_pad(pos, result)


action()

# 67486 to high
