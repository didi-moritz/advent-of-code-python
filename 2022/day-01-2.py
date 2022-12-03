with open('day-01.data') as f:
    data = [line.rstrip('\n') for line in f]

current = 0
sums = []


def store_sum():
    global current
    sums.append(current)
    current = 0


for n in data:
    if n == '':
        store_sum()
    else:
        current = current + int(n)

store_sum()

sums.sort(reverse=True)

print(sums[0] + sums[1] + sums[2])
