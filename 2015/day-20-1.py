target = 34000000
target /= 10


def calc_presents(house_nr):
    presents = house_nr + 1 if house_nr > 1 else 1
    for elf in range(2, int(house_nr / 2) + 1):
        if house_nr != elf and house_nr % elf == 0:
            presents += elf

    return presents


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

min_house_nr = -1


def action(house_nr, min_prime):
    global min_house_nr

    if 0 < min_house_nr <= house_nr:
        return

    presents = calc_presents(house_nr)

    if presents >= target:
        if house_nr < min_house_nr or min_house_nr < 0:
            print(house_nr)
            min_house_nr = house_nr
        return

    for prime in primes:
        if prime >= min_prime:
            action(house_nr * prime, prime)


action(1, 1)

print(min_house_nr)
