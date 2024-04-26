from random import randint

n = 10

r = randint(1, 1000)
c = randint(1, 1000)

sr, sc = r, c
lr, lc = 0, 0
print(n)
direction = randint(0, 3)
for _ in range(n-1):
    direction += randint(0, 3)
    if (direction) % 4 == 0:
        r, c = r + randint(1, 1000-r), c
    elif direction % 4 == 1:
        r, c = r, c + randint(1, 1000-c)
    elif direction % 4 == 2:
        r, c = r-randint(1, r), c
    elif direction % 4 == 3:
        r, c = r, c-randint(1, c)
    print(r, c)
    lr, lc = r, c
print(sr, lc)
