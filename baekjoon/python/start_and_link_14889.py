# Title: 스타트와 링크
# Link: https://www.acmicpc.net/problem/14889

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def dfs(n: int, ans: list, depth: int, target: int, special: list, team: list, all_cases: list):
    if depth == target:
        all_cases.append(ans[0])
    else:
        for i in range(n+1, target*2+1):
            for member in team:
                ans[0] += (special[member][i]+special[i][member])
            team.append(i)
            dfs(i, ans, depth+1, target, special, team, all_cases)
    team.pop()
    for member in team:
        ans[0] -= (special[member][n]+special[n][member])


def solution(n: int, s: list):
    all_cases = []
    ans = [0]

    for i in range(1, n-n//2+2):
        dfs(i, ans, 1, n//2, s, [i], all_cases)

    min_diff = 9999999999999
    all_cases = deque(all_cases)
    while all_cases:
        min_diff = min(min_diff, abs(all_cases.popleft() - all_cases.pop()))
    return min_diff


def main():
    n = read_single_int()
    s = []
    s.append([0]*-~n)
    for _ in range(n):
        s.append([0] + read_list_int())
    print(solution(n, s))


if __name__ == '__main__':
    main()