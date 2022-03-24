# Title: /\/\/\/
# Link: https://arc103.contest.atcoder.jp/tasks/arc103_a

import sys
import collections

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, vs: list):
    map_a = collections.defaultdict(lambda: 0)
    map_b = collections.defaultdict(lambda: 0)

    for i in range(0, n, 2):
        map_a[vs[i]] += 1
        map_b[vs[i+1]] += 1

    pair_a = [(k, map_a[k]) for k in map_a.keys()]        
    pair_b = [(k, map_b[k]) for k in map_b.keys()]

    pair_a = sorted(pair_a, key=lambda x: x[1], reverse= True)
    pair_b = sorted(pair_b, key=lambda x: x[1], reverse= True)

    first_a, second_a = pair_a[0], (0, 0) if len(pair_a) == 1 else pair_a[1]
    first_b, second_b = pair_b[0], (0, 0) if len(pair_b) == 1 else pair_b[1]

    if first_a[0] != first_b[0]:
        return n//2-first_a[1] + n//2-first_b[1]
    else:
        if first_a[1] + second_b[1] < second_a[1] + first_b[1]:
            return n//2-second_a[1] + n//2-first_b[1]

    return n//2-first_a[1] + n//2-second_b[1]


def main():
    n = read_single_int()
    vs = read_list_int()
    print(solution(n, vs))


if __name__ == '__main__':
    main()