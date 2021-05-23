# Title: 선물 교환
# Link: https://www.acmicpc.net/problem/19596

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

q = [deque() for _ in range(1010)]
check = [0 for _ in range(1001001)]
x = [0 for _ in range(1001001)]
y = [0 for _ in range(1001001)]
# s = [0 for _ in range(1010)]


def dfs(u: int, flag: int):
    if flag:
        if len(q[u])%2:
            # s[u]-=1
            return
        # else:
            # s[u]-=1

    while check[q[u][0]]:
        q[u].popleft()
    id = q[u][0]
    q[u].popleft()
    # s[u] -= 1
    check[id] = 1 if u == x[id] else 2
    dfs(y[id] if u == x[id] else x[id], 1)


def main():
    t = read_single_int()
    for _ in range(t):
        n, m = read_list_int()

        for i in range(n+1):
            if q[i]:
                q[i].clear()
            # s[i] = 0

        for i in range(m+1):
            check[i] = 0

        for i in range(1, m+1):
            x[i], y[i] = read_list_int()
            q[x[i]].append(i)
            q[y[i]].append(i)
            # s[x[i]]+=1
            # s[y[i]]+=1

        for i in range(1, n+1):
            if len(q[i]) % 2:
                dfs(i, 0)
        
        for i in range(1, n+1):
            while q[i]:
                dfs(i, 0)

        print(''.join(map(lambda e: str(e-1), check[1:m+1])))


if __name__ == '__main__':
    main()