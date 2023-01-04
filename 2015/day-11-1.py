input = 'cqjxjnds'

number = [ord(c) for c in input]

digits = []
for i in range(ord('a'), ord('z') + 1):
    digits.append(i)
digits.remove(ord('i'))
digits.remove(ord('o'))
digits.remove(ord('l'))

while True:
    for i in range(7, -1, -1):
        if number[i] == ord('z'):
            number[i] = ord('a')
            continue

        number[i] = digits[digits.index(number[i]) + 1]
        break

    check = False
    for i in range(0, 8 - 2):
        if number[i] == (number[i + 1] - 1) == (number[i + 2] - 2):
            check = True
            break

    if not check:
        continue

    first_pair = 0
    for i in range(0, 8 - 3):
        if number[i] == number[i + 1]:
            first_pair = number[i]
            break

    if not first_pair:
        continue

    second_pair = 0
    for i in range(2, 8 - 1):
        if number[i] == number[i + 1] and number[i] != first_pair:
            second_pair = number[i]
            break

    if not second_pair:
        continue

    break

for n in number:
    print(chr(n), end='')
print()
