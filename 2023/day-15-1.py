with open('day-15.data') as f:
    data = [line.rstrip('\n') for line in f]


def hash_word(word):
    value = 0
    for c in word:
        value += ord(c)
        value *= 17
        value %= 256

    return value


def action():
    words = data[0].split(',')

    result = 0

    for word in words:
        result += hash_word(word)

    return result


print(action())

# 88032 too low
