with open('day-03.data') as f:
    data = [line.rstrip('\n') for line in f]


def calc_priority(c):
    return ord(c) - (ord('a') if ord(c) > ord('Z') else (ord('A') - 26)) + 1


score = 0
for i in range(0, len(data), 3):
    for j in data[i]:
        if j in data[i + 1] and j in data[i + 2]:
            print(data[i])
            print(data[i + 1])
            print(data[i + 2])
            print(f' ->  {j} -> {calc_priority(j)}  -> {score}')
            score += calc_priority(j)
            break

print(score)
