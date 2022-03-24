import random

n = random.randint(0, 7)
m = random.randint(0, 7)

print('{} {}'.format(n, m))

for _ in range(n+m):
    a = random.randint(1, 12)
    h = random.randint(1, 12)
    print('{} {}'.format(a, h))