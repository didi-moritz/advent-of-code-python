with open('day-17.data') as f:
    data = [line.rstrip('\n') for line in f]

containers = [int(n) for n in data]

TARGET_LITERS = 150

possibilities = 0


def action(liter_index, liters):
    global possibilities

    if liters == TARGET_LITERS:
        possibilities += 1
        return

    if liters > TARGET_LITERS:
        return

    for i in range(liter_index + 1, len(containers)):
        action(i, liters + containers[i])


action(-1, 0)

print(possibilities)
