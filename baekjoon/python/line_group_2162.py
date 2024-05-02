# Title: 선분 그룹
# Link: https://www.acmicpc.net/problem/2162

import sys
from collections import defaultdict


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


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


def ccw(ax, ay, bx, by, cx, cy) -> int:
    t = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
    if t > 0:
        return 1
    elif t < 0:
        return -1
    return 0


def intersect(ax, ay, bx, by, cx, cy, dx, dy) -> bool:
    c1 = ccw(ax, ay, bx, by, cx, cy)
    c2 = ccw(ax, ay, bx, by, dx, dy)
    c3 = ccw(cx, cy, dx, dy, ax, ay)
    c4 = ccw(cx, cy, dx, dy, bx, by)
    if c1 * c2 > 0 or c3 * c4 > 0:
        return False
    elif c1 or c2 or c3 or c4:
        return True
    elif min(ax, ax) > max(cx, dx) or\
            min(ay, by) > max(cy, dy) or\
            min(cx, dx) > max(ax, bx) or\
            min(cy, dy) > max(ay, by):
        return False
    return True


def solution(n: int, lines: list) -> str:
    uf = UnionFind(n)
    for i, first_line in enumerate(lines):
        for j, second_line in enumerate(lines[i+1:], i+1):
            if intersect(*first_line, *second_line):
                uf.union(i, j)

    groups = defaultdict(lambda: 0)

    for i in range(0, n):
        groups[uf.find(i)] += 1
    max_group = max(list(groups.values()))

    return f"{len(groups)}\n{max_group}"


def main():
    n = read_single_int()
    lines = []
    for _ in range(n):
        lines.append(read_list_int())
    print(solution(n, lines))


if __name__ == '__main__':
    main()
