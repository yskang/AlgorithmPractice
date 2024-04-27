from random import randint

cards = [randint(0, 5) for _ in range(10)]

print(' '.join(map(str, cards)))
