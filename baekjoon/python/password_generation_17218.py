# Title: 비밀번호 만들기
# Link: https://www.acmicpc.net/problem/17218

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: list(sys.stdin.readline().strip())


def solution(a: str, b: str):
    a, b = [''] + a, [''] + b
    height, width = len(a), len(b)

    dp = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(1, height):
        for x in range(1, width):
            if a[y] == b[x]:
                dp[y][x] = dp[y-1][x-1] + 1
            else:
                dp[y][x] = max(dp[y-1][x], dp[y][x-1])
    
    ans = []

    start_x, start_y = width-1, height-1
    prev_num = dp[start_y][start_x]

    while True:
        while True:
            start_y -= 1
            if dp[start_y][start_x] != prev_num:
                start_y += 1
                break
        while True:
            start_x -= 1
            if dp[start_y][start_x] != prev_num:
                start_x += 1
                break

        ans.append(b[start_x])
        start_x -= 1
        prev_num = dp[start_y][start_x]
        if prev_num == 0:
            break

    return ''.join(reversed(ans))


def main():
    a = read_single_str()
    b = read_single_str()
    print(solution(a, b))


if __name__ == '__main__':
    main()