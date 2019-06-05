# Title: 마약수사대
# Link: https://www.acmicpc.net/problem/17220

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


def dfs(node: int, childs_of: list, visited: list):
    if visited[node]:
        return
    visited[node] = True

    for child in childs_of[node]:
        dfs(child, childs_of, visited)


def solution(n: int, m: int, childs_of: list, knowns: list, supplies: list):
    visited = [False for _ in range(n)]
    for node in knowns[1:]:
        node = ord(node) - ord('A')
        dfs(node, childs_of, visited)

    count = 0
    for is_supply, visit in list(zip(supplies, visited)):
        if not is_supply and not visit:
            count += 1

    return count


def main():
    n, m = read_list_int()
    childs_of = [[] for _ in range(n)]
    supplies = [True for _ in range(n)]
    for _ in range(m):
        a, b = read_list_words()
        a = ord(a) - ord('A')
        b = ord(b) - ord('A')
        childs_of[a].append(b)
        supplies[b] = False
    knowns = read_list_words()
    print(solution(n, m, childs_of, knowns, supplies))


if __name__ == '__main__':
    main()