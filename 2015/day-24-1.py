with open('day-24.data') as f:
    data = [line.rstrip('\n') for line in f]


def load():
    ps = list(map(int, data))

    s = 0
    for p in ps:
        s += p

    t = int(s / 3)

    return [ps, t]


packages, target = load()

print(packages)

min_count = 0
min_quantum = 0


def action(selected: [int], pos):
    global min_count
    global min_quantum

    quantum = 1
    s = 0
    for p in selected:
        s += p
        quantum *= p

    if min_quantum and len(selected) >= min_count and quantum >= min_quantum:
        return

    if s == target:
        if not min_count or len(selected) < min_count or not min_quantum or quantum < min_quantum:
            min_quantum = quantum
            min_count = len(selected)
            print(selected)
        return

    if s > target:
        return

    for i in range(pos + 1, len(packages)):
        action(selected + [packages[i]], i)


action([], -1)

print(min_count)
print(min_quantum)
