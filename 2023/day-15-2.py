import collections

with open('day-15.data') as f:
    data = [line.rstrip('\n') for line in f]


def hash_word(label):
    value = 0
    for c in label:
        value += ord(c)
        value *= 17
        value %= 256

    return value


boxes = [collections.OrderedDict() for i in range(256)]


def process_word(word):
    global boxes

    if word[-1] == '-':
        label = word[:-1]
        if label in boxes[hash_word(label)]:
            del boxes[hash_word(label)][label]
    else:
        label, focal_length_text = word.split('=')
        focal_length = int(focal_length_text)
        boxes[hash_word(label)][label] = focal_length


def action():
    words = data[0].split(',')

    for word in words:
        process_word(word)

    result = 0

    for i in range(256):
        j = 1
        for value in boxes[i].values():
            result += (i + 1) * j * value
            j += 1

    return result


print(action())
