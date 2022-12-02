with open('day-01-1.data') as f:
    data = [line.rstrip('\n') for line in f]

max = 0
current = 0


def check():
    global max, current
    if current > max:
        max = current
    current = 0


for n in data:
    if n == '':
        check()
    else:
        current = current + int(n)

check()

print(max)
