from random import randint

n = randint(2, 100000)
ss = [randint(1, 1000) for _ in range(n)]
pos = set()
while True:
    x = randint(1, 1000000)
    y = randint(1, 1000000)
    pos.add('{} {}'.format(x, y))
    if len(pos) == n:
        break
print(n)
print(*ss)
for xy in pos:
    print(xy)
