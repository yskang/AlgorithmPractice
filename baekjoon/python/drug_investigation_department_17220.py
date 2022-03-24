# Title: 마약수사대
# Link: https://www.acmicpc.net/problem/17220

import sys


sys.setrecursionlimit(10 ** 6)

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


def dfs(node: int, childs_of: list, visited: list, knowns: list):
    if visited[node]:
        return
    visited[node] = True

    if node not in knowns:
        for child in childs_of[node]:
            dfs(child, childs_of, visited, knowns)


def solution(n: int, m: int, childs_of: list, knowns: list, sources: list):
    visited = [False for _ in range(n)]

    for node, is_supply in enumerate(sources):
        if is_supply:
            dfs(node, childs_of, visited, knowns)

    for node in knowns:
            visited[node] = False

    count = 0
    for is_visit, is_source in list(zip(visited, sources)):
        if is_visit and not is_source:
            count += 1
    return count


def main():
    n, m = read_list_int()
    childs_of = [[] for _ in range(n)]
    sources = [True for _ in range(n)]
    for _ in range(m):
        a, b = read_list_words()
        a = ord(a) - ord('A')
        b = ord(b) - ord('A')
        childs_of[a].append(b)
        sources[b] = False
    knowns = read_list_words()
    knowns = list(map(lambda x: ord(x)-ord('A'), knowns[1:]))
    print(solution(n, m, childs_of, knowns, sources))


if __name__ == '__main__':
    main()