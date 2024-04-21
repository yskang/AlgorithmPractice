from random import randint

n = randint(7, 7)
m = randint(7, 7)
k = randint(1, 1)
a = [randint(0, 2) for _ in range(n)]
print(f'{n} {m} {k}')
print(' '.join(map(str, a)))
for _ in range(m):
    print(f'{randint(1, n)} {randint(1, n)} {randint(1, 10)}')
for _ in range(k):
    print(randint(1, n))
