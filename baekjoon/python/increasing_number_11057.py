# Title: 오르막 수
# Link: https://www.acmicpc.net/problem/11057

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    if n == 1:
        return 10
        
    d = [[0 for _ in range(10)] for _ in range(n+1)]

    for i in range(10):
        d[1][i] = 1

    for num_len in range(2, n+1):
        for num in range(10):
            s = 0
            for i in range(num+1):
                s += d[num_len-1][i]
            d[num_len][num] = s

    ans = 0
    for i in range(10):
        ans += d[n][i]
    return ans % 10007



def main():
    N = read_single_int()
    print(solution(N))


if __name__ == '__main__':
    main()