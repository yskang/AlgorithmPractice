# Title: Manhattan Crepe Cart
# Link: hhttps://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c

import sys
import bisect

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


def solution(p: int, q: int, persons: list):
    norths = []
    souths = []
    easts = []
    wests = []
    for x, y, d in persons:
        if d == 'N':
            norths.append(y)
        elif d == 'S':
            souths.append(y)
        elif d == 'E':
            easts.append(x)
        elif d == 'W':
            wests.append(x)
    norths = sorted(norths)
    souths = sorted(souths)

    ys = set(norths)
    ys.update(souths)
    ys = sorted(ys)
    ys = list(map(lambda k: k+1, ys))
    
    max_y_value = -99999
    max_y = -99999
    for y in [0] + ys:
        v = bisect.bisect_left(norths, y)
        v += (len(souths) - bisect.bisect_right(souths, y))
        if v > max_y_value:
            max_y_value = v
            max_y = y

    wests = sorted(wests)
    easts = sorted(easts)

    xs = set(wests)
    xs.update(easts)
    xs = sorted(xs)
    xs = list(map(lambda k: k+1, xs))

    max_x_value = -9999
    max_x = -9999
    for x in [0] + xs:
        v = bisect.bisect_left(easts, x)
        v += (len(wests)-bisect.bisect_right(wests, x))
        if v > max_x_value:
            max_x_value = v
            max_x = x
    return '{} {}'.format(max_x, max_y)


def main():
    t = read_single_int()
    for case in range(1, t+1):
        p, q = read_list_int()
        persons = []
        for _ in range(p):
            x, y, d = read_list_words()
            persons.append((int(x), int(y), d))
        print('Case #{}: {}'.format(case, solution(p, q, persons)))


if __name__ == '__main__':
    main()