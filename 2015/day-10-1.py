number = '1113122113'

for i in range(40):
    current = 0
    count = 0
    result = ''
    for j in range(len(number) + 1):
        c = number[j] if j < len(number) else 0
        if c == current:
            count += 1
        else:
            if count > 0:
                result += f'{count}{current}'
            current = c
            count = 1

    number = result

print(len(number))
