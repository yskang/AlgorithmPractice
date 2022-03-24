# Title: 선물 교환
# Link: https://www.acmicpc.net/problem/gifts

import sys
from collections import defaultdict
from typing import DefaultDict, Set, List

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, child_of: DefaultDict, values: DefaultDict, odds: List):
    res = ['0' for _ in range(m)]

    dummy = n+1
    while odds:
        x, y = odds.pop(), odds.pop()
        child_of[x].add(dummy)
        child_of[y].add(dummy)
        child_of[dummy].add(x)
        child_of[dummy].add(y)

    ans = []
    while True:
        start = None
        for node in child_of:
            if child_of[node]:
                start = node
                break
        else:
            break
        st = [start]
        while st:
            v = st[-1]
            if not child_of[v]:
                ans.append(v)
                st.pop()
            else:
                to = child_of[v].pop()
                child_of[to].discard(v)
                st.append(to)

    for i in range(len(ans)-1):
        v = (ans[i], ans[i+1])
        if v in values:
            res[values[v]] = '1'

    return ''.join(res)


def main():
    t = read_single_int()
    for _ in range(t):
        n, m = read_list_int()
        child_of = defaultdict(lambda: set())
        values = defaultdict(lambda: 0)
        for i in range(m):
            x, y = read_list_int()
            child_of[x].add(y)
            child_of[y].add(x)
            values[(x, y)] = i
        odds = []
        for i in child_of:
            if len(child_of[i]) % 2:
                odds.append(i)
        print(solution(n, m, child_of, values, odds))


if __name__ == '__main__':
    main()