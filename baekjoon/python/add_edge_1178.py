# Title: 간선 추가
# Link: https://www.acmicpc.net/problem/1178

import sys
from collections import defaultdict
from heapq import heappop, heappush


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


class UnionFind:
    def __init__(self, max_count):
        self.p = [-1 for _ in range(max_count)]

    def find(self, a: int):
        if self.p[a] < 0:
            return a
        self.p[a] = self.find(self.p[a])
        return self.p[a]

    def union(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.p[a] < self.p[b]:
            self.p[a] += self.p[b]
            self.p[b] = a
        else:
            self.p[b] += self.p[a]
            self.p[a] = b
        return True

    def size(self, a: int):
        return -self.p[self.find(a)]


def solution(v: int, e: int, graph: list, uf: UnionFind) -> int:
    odds = set()
    evens = set()
    groups = defaultdict(lambda: [])

    for i in range(1, v+1):
        groups[uf.find(i)].append(i)
        if len(graph[i]) % 2 == 1:
            odds.add(i)
        else:
            evens.add(i)
    group_info = []

    for group in groups:
        odd_num, even_num = 0, 0
        for node in set(groups[group] + [group]):
            if node in odds:
                odd_num += 1
            else:
                even_num += 1
        heappush(group_info, (-odd_num, -even_num, group))  # odd_num, even_num, group_id

    ans = 0

    while len(group_info) > 1:
        odd_num1, even_num1, group1 = heappop(group_info)
        odd_num2, even_num2, group2 = heappop(group_info)
        odd_num1, odd_num2 = -odd_num1, -odd_num2
        even_num1, even_num2 = -even_num1, -even_num2
        merged_odd, merged_even = 0, 0
        if odd_num1 > 0 and odd_num2 > 0:
            merged_odd = odd_num1 + odd_num2 - 2
            merged_even = even_num1 + even_num2 + 2
        elif odd_num1 > 0 and odd_num2 == 0:
            merged_odd = odd_num1
            merged_even = even_num1 + even_num2
        elif odd_num1 == 0 and odd_num2 == 0:
            merged_odd = 2
            merged_even = even_num1 + even_num2 - 2
        elif odd_num1 == 0 and odd_num2 > 0:
            merged_odd = odd_num2
            merged_even = even_num1 + even_num2
        ans += 1
        heappush(group_info, (-merged_odd, -merged_even, group1))

    odd_num, even_num, group = heappop(group_info)
    odd_num, even_num = -odd_num, -even_num

    if odd_num == 0 or odd_num == 2:
        return ans
    return ans + (odd_num - 2) // 2


def main():
    v, e = read_list_int()
    graph = [[] for _ in range(v+1)]
    uf = UnionFind(v+1)
    for _ in range(e):
        a, b = read_list_int()
        graph[a].append(b)
        graph[b].append(a)
        uf.union(a, b)
    print(solution(v, e, graph, uf))


if __name__ == '__main__':
    main()
