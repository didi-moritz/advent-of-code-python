with open('day-10.data') as f:
    data = [line.rstrip('\n') for line in f]

x = 1
cycle = 1
score = 0


def check_cycle():
    if (cycle - 1) % 40 == 0:
        print()
    if x <= (cycle % 40) < x + 3:
        print('#', end='')
    else:
        print('.', end='')


for line in data:
    if line.startswith('addx'):
        v = int(line.split(' ')[1])
        check_cycle()
        cycle += 1
        check_cycle()
        x += v
        cycle += 1
    else:
        check_cycle()
        cycle += 1
