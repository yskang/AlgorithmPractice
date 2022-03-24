import sys
import random
from collections import defaultdict

def main():
    n = random.randint(3, 5)
    print(n)
    dots = defaultdict(lambda:0)
    while len(dots) < n:
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        dots[(x, y)] += 1
        if dots[(x, y)] == 1:
            print('{} {}'.format(x, y))


if __name__ == '__main__':
    main()