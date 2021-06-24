from random import randint

n = randint(1, 10)
m = randint(1, 10)

print(f'{n} {m}')

for _ in range(m):
    while True:
        a = randint(1, n)
        b = randint(1, n)
        if a != b:
            print(f'{a} {b}')
            break
        