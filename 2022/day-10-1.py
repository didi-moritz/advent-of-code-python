with open('day-10.data') as f:
    data = [line.rstrip('\n') for line in f]

x = 1
cycle = 1
score = 0


def check_cycle():
    global score
    if cycle % 40 == 20:
        print(f'{cycle} -> {x}')
        score += (cycle * x)


for line in data:
    if line.startswith('addx'):
        v = int(line.split(' ')[1])
        cycle += 1
        check_cycle()
        x += v
        cycle += 1
        check_cycle()
    else:
        cycle += 1
        check_cycle()

print(score)
