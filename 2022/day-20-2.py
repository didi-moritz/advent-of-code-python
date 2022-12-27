with open('day-20.data') as f:
    data = [int(line.rstrip('\n')) for line in f]

description_key = 811589153


class Item:
    def __init__(self, index, value):
        self.index = index
        self.value = value


n: list[Item] = []
for i in range(len(data)):
    n.append(Item(i, data[i] * description_key))

length = len(n)

for j in range(10):
    for i in range(length):
        for k in range(length):
            if n[k].index == i:
                item = n[k]
                pos = k
                break

        n = n[pos + 1:length] + n[0:pos]

        steps = item.value % (length - 1)

        n = n[0:steps] + [item] + n[steps:len(n)]

        if len(n) != length:
            exit(0)

for k in range(length):
    if n[k].value == 0:
        index_0 = k
        break

r_1 = n[(index_0 + 1000) % length].value
r_2 = n[(index_0 + 2000) % length].value
r_3 = n[(index_0 + 3000) % length].value

print(r_1)
print(r_2)
print(r_3)
print('=' * 4)
print(r_1 + r_2 + r_3)
