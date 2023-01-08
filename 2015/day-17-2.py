with open('day-17.data') as f:
    data = [line.rstrip('\n') for line in f]

containers = [int(n) for n in data]

TARGET_LITERS = 150

possibilities = 0
min_container = len(containers)


def action(liter_index, liters, container_count):
    global possibilities
    global min_container

    if liters == TARGET_LITERS:
        if container_count <= min_container:
            if container_count < min_container:
                min_container = container_count
                possibilities = 0
            possibilities += 1
        return

    if liters > TARGET_LITERS:
        return

    for i in range(liter_index + 1, len(containers)):
        action(i, liters + containers[i], container_count + 1)


action(-1, 0, 0)

print(possibilities)
