# Title: 그래서 팩 주냐?
# Link: https://www.acmicpc.net/problem/17227

import sys
from collections import defaultdict, deque
from types import SimpleNamespace
from operator import add

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 10**10


def dfs(cur: int, is_joonpyo: bool, dp: list, child_of: defaultdict):
    if dp[cur][is_joonpyo] != -1:
        return dp[cur][is_joonpyo]
    ret = INF
    if is_joonpyo:
        size = len(child_of[cur])
        for child in child_of[cur]:
            dfs(child, not is_joonpyo, dp, child_of)
        child_of[cur] = sorted(child_of[cur], key=lambda x: dp[x][0], reverse=True)
        for i in range(size):
            ret = min(ret, dp[child_of[cur][i]][0] + i)
    else:
        for child in child_of[cur]:
            ret = min(ret, dfs(child, not is_joonpyo, dp, child_of))
    dp[cur][is_joonpyo] = ret
    return ret


def solution(n: int, e: int, child_of: defaultdict, starts: list):
    ans = INF
    dp = [[-1, -1] for _ in range(n+1)]
    dp[n][1] = 0   # Joonpyo
    dp[n][0] = INF # manyoung
    for start_node in starts:
        ans = min(ans, dfs(start_node, True, dp, child_of))
    return ans if ans != INF else -1

def main():
    n, e = read_list_int()
    child_of = defaultdict(lambda: [])
    starts = [SimpleNamespace(index= i, value= True) for i in range(n+1)]
    for _ in range(e):
        a, b = read_list_int()
        child_of[a].append(b)
        starts[b].value = False
    starts = list(map(lambda x: x.index, filter(lambda x: x.value, starts)))
    print(solution(n, e, child_of, starts[1:]))


if __name__ == '__main__':
    main()