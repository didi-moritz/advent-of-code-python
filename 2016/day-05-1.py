from hashlib import md5

door_id = 'reyedfim'

result = ''
i = 0

while len(result) < 8:
    text = f'{door_id}{i}'
    code = md5(text.encode()).hexdigest()
    if code.startswith('00000'):
        result += code[5]
        print(result)

    i += 1
