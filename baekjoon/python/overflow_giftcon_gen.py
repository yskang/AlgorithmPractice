from random import randint

n = randint(4, 4)
vs = [randint(1, 10) for _ in range(n)]
ds = [randint(1, 10) for _ in range(n)]

print(n)
print(*vs)
print(*ds)