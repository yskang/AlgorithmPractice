# Title: 욱제가 풀어야 하는 문제
# Link: https://www.acmicpc.net/problem/18249

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


MOD = 10**9+7


def main():
    t = read_single_int()
    queries = []
    
    for _ in range(t):
        queries.append(read_single_int())
    
    max_query = max(queries)

    ans = [0, 1, 2]

    for i in range(3, max_query+1):
        ans.append((ans[-1]+ans[-2])%MOD)

    for query in queries:
        print(ans[query])


if __name__ == '__main__':
    main()