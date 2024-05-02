from random import randint

n = randint(2, 10)
print(n)

ps = set()

while len(ps) < n:
    ps.add(randint(1, 1000))

for _ in range(n):
    c = randint(1, 1000)
    print(f'{ps.pop()} {c}')
