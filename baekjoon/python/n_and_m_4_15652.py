# Title: N과 M (4)
# Link: https://www.acmicpc.net/problem/15652

import sys


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int):
    ans = [1 for _ in range(m)]
    print(*ans)
    while True:
        for i in range(m-1, -1, -1):
            if ans[i] < n:
                ans[i] += 1
                break
            else:
                if i == 0:
                    return
                x = 1
                while i-x >= 0:
                    if ans[i-x] < n:
                        ans[i] = ans[i-x]+1
                        break
                    else:
                        x+=1

        print(*ans)


def main():
    n, m = read_list_int()
    solution(n, m)


if __name__ == '__main__':
    main()