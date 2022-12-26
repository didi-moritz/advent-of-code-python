with open('day-20.data') as f:
    data = [int(line.rstrip('\n')) for line in f]

n = data.copy()

length = len(n)

print(n)

for i in data:
    pos = n.index(i)
    n = n[pos + 1:length] + n[0:pos]

    steps = i % len(n)

    while steps < 0:
        steps += len(n)

    n = n[0:steps] + [i] + n[steps:len(n)]

index_0 = n.index(0)

r_1 = n[(index_0 + 1000) % length]
r_2 = n[(index_0 + 2000) % length]
r_3 = n[(index_0 + 3000) % length]

print(r_1)
print(r_2)
print(r_3)
print('=' * 4)
print(r_1 + r_2 + r_3)
