# Title: 빗물이 넘쳐흘러
# Link: https://www.acmicpc.net/problem/17421

import sys
from types import SimpleNamespace


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, k: int, ds: list):
    max_cols = [SimpleNamespace(depth=0, index=-1)]
    prev_depth = 0
    for i, depth in enumerate(ds):
        if prev_depth > depth:
            while max_cols:
                if max_cols[-1].depth <= depth:
                    max_cols.append(SimpleNamespace(depth=depth, index=i))
                    break
                else:
                    max_cols.pop()
            if not max_cols:
                return -1
        elif prev_depth < depth:
            if len(max_cols) == k:
                total = 0
                prev = max_cols[0]
                for col in max_cols[1:]:
                    total += sum(map(lambda x: 0 if x < col.depth else x-col.depth, ds[prev.index+1: col.index]))
                    prev = col

                return total
        prev_depth = depth

    return -1


def main():
    n, k = read_list_int()
    ds = read_list_int() + [0]
    print(solution(n, k, ds))


if __name__ == '__main__':
    main()