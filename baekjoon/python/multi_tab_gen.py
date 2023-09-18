from random import randint

n = randint(1, 100)
k = randint(1, 100)

print(f'{n} {k}')
nums = []
for _ in range(k):
    nums.append(randint(1, 100))

print(' '.join(map(str, nums)))