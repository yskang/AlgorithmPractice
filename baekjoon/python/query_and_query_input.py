import random

n = random.randint(1, 100000)
m = random.randint(1, 100000)
q = random.randint(1, 100000)

print(f'{n} {m} {q}')

a_list = [random.randint(0, 10**9) for _ in range(n)]

print(*a_list)

for _ in range(m):
    l = random.randint(1, n)
    r = random.randint(l, n)
    x = random.randint(0, 10**9)
    print(f'{l} {r} {x}')

for _ in range(q):
    k = random.randint(1, 2)
    if k == 1:
        l = random.randint(1, m)
        r = random.randint(l, m)
        v = random.randint(0, 10**9)
        print(f'1 {l} {r} {v}')
    else:
        s = random.randint(1, n)
        e = random.randint(s, n)
        print(f'2 {s} {e}')
