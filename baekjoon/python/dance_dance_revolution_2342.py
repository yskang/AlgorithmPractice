# Title: Dance Dance Revolution
# Link: https://www.acmicpc.net/problem/2342

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def effort(prev_pos: int, next_pos: int):
    if prev_pos == next_pos:
        return 1
    elif prev_pos == 0:
        return 2
    elif abs(prev_pos - next_pos) == 2:
        return 4
    else:
        return 3


def get_min_effort(left: int, right: int, cmd_idx: int, dp: list, cmds: list):
    if cmd_idx == len(cmds)-1:
        return 0

    if dp[left][right][cmd_idx] != -1:
        return dp[left][right][cmd_idx]

    ans = 0

    left_move = get_min_effort(cmds[cmd_idx], right, cmd_idx+1, dp, cmds) + effort(left, cmds[cmd_idx])
    right_move = get_min_effort(left, cmds[cmd_idx], cmd_idx+1, dp, cmds) + effort(right, cmds[cmd_idx])

    ans = min(left_move, right_move)
    dp[left][right][cmd_idx] = ans
    return ans


def solution(cmds: list):
    dp = [[[-1 for _ in range(len(cmds)+1)] for _ in range(5)] for _ in range(5)]
    ans = get_min_effort(0, 0, 0, dp, cmds)
    return ans


def main():
    n = read_list_int()
    print(solution(n))


if __name__ == '__main__':
    main()