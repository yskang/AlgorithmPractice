import random

a = random.randint(0, 3)
b = random.randint(0, 3)
n = random.randint(1, 10)
times = [i for i in range(1, 30)]
random.shuffle(times)
times = times[:n]
times = sorted(times, reverse=True)
print(a, b, n)
color = ['R', 'B']
for _ in range(n):
    print(times.pop(), color[random.randint(0, 1)], random.randint(1, 5))