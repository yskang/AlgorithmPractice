from random import randint

n = randint(7, 7)
m = randint(7, 7)

print(f'{n} {m}')
for _ in range(n):
    row = []
    for _ in range(m):
        row.append("ABCD"[randint(0, 3)])
    print("".join(row))
