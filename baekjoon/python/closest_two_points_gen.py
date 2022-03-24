from random import randint

n = randint(2, 10)
print(n)
dots = set()
while len(dots) != n:
    dots.add((randint(0, 10), randint(0, 10)))

for x, y in dots:
    print('{} {}'.format(x, y))