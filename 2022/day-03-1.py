with open('day-03.data') as f:
    data = [line.rstrip('\n') for line in f]


def find_item(line: str) -> int:
    second = line[int(len(line) / 2):]
    for i in line:
        if i in second:
            points = ord(i) - (ord('a') if ord(i) > ord('3') else (ord('A') - 26)) + 1
            print(f'{line} -> {second} -> {i} -> {points}')
            return points


score = 0
for line in data:
    score += find_item(line)

print(score)
