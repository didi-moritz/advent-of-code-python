with open('day-19.data') as f:
    data = [line.rstrip('\n') for line in f]

rules = []


def load():
    for i in range(len(data) - 2):
        rules.append(tuple(data[i].split(' => ')))


load()

word = data[-1]


def action():
    words = set()
    for rule in rules:
        last_pos = 0
        while True:
            pos = word.find(rule[0], last_pos)
            if pos >= 0:
                new_word = word[:pos] + rule[1] + word[pos + len(rule[0]):]
                words.add(new_word)
                last_pos = pos + 1
            else:
                break

    return len(words)


print(action())
