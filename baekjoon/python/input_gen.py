from random import randint

v = randint(2, 5)
e = randint(1, v*(v-1)//2)

print(v, e)
for _ in range(e):
    print(randint(1, v), randint(1, v))
