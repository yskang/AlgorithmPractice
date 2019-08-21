# Title: 3루수는 몰라
# Link: https://www.acmicpc.net/problem/17351

import sys
from types import SimpleNamespace


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(n: int, ground: list):
    dp = [[SimpleNamespace(status=False, count=0) for _ in range(-~n)] for _ in range(-~n)]
    for y in range(1, -~n):
        for x in range(1, -~n):
            current_char = ground[y][x]

            count_from_up = dp[y-1][x].count
            count_from_left = dp[y][x-1].count

            status_from_up = dp[y-1][x].status
            status_from_left = dp[y][x-1].status

            if current_char == 'M':
                dp[y][x].count = max(count_from_up, count_from_left)
                dp[y][x].status = True
                continue
            elif current_char == 'A':
                if status_from_up and ground[y-1][x] == 'L':
                    count_from_up += 1
                if status_from_left and ground[y][x-1] == 'L':
                    count_from_left += 1
            elif current_char == 'O':
                if status_from_up and ground[y-1][x] != 'M':
                    status_from_up = False
                if status_from_left and ground[y][x-1] != 'M':
                    status_from_left = False
            elif current_char == 'L':
                if status_from_up and ground[y-1][x] != 'O':
                    status_from_up = False
                if status_from_left and ground[y][x-1] != 'O':
                    status_from_left = False
            else:
                status_from_left = False
                status_from_up = False

            if count_from_up > count_from_left:
                dp[y][x].count = count_from_up
                dp[y][x].status = status_from_up
            elif count_from_left > count_from_up:
                dp[y][x].count = count_from_left
                dp[y][x].status = status_from_left
            else:
                dp[y][x].count = count_from_up
                dp[y][x].status = status_from_left | status_from_up

    return dp[n][n].count


def main():
    n = read_single_int()
    ground = []
    ground.append(['X']*-~n)
    for _ in range(n):
        ground.append(['X']+read_list_str())
    print(solution(n, ground))


if __name__ == '__main__':
    main()