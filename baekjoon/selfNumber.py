from functools import reduce

numbers = list(range(1, 10001))

def d(n):
    return n + reduce(lambda x, y: x + y, list(map(int, list(str(n)))))

for i in numbers:
    if i != 0:
        next = d(i)
        # numbers.remove(1)

        while True:
            if next > 10000:
                break
            numbers[next-1] = 0
            next = d(next)

for i in numbers:
    if i != 0:
        print(i)
