# Title: 여우가 정보섬에 올라온 이유
# Link: https://www.acmicpc.net/problem/17131

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

MOD = 1000000007

class Segment_Tree:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(len(self.array) * 4)]
        self.init(self.tree, 0, len(self.array)-1, 1)
        self.last_index = len(array)-1

    def init(self, tree, start, end, node):
        if start == end:
            tree[node] = self.array[start]
            return tree[node]
        mid = (start + end) // 2
        tree[node] = self.init(tree, start, mid, node * 2) + self.init(tree, mid + 1, end, node * 2 + 1)
        return tree[node]

    def sum(self, left, right, node=1, start=0, end=-1):
        if end == -1:
            end = self.last_index
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        return self.sum(left, right, node*2, start, (start+end)//2) + self.sum(left, right, node*2+1, (start+end)//2+1, end)

    def update(self, index, diff, node=1, start=0, end=-1):
        if end == -1:
            end = self.last_index
        if not(start <= index <= end):
            return
        self.tree[node] += diff
        if start != end:
            self.update(index, diff, node*2, start, (start+end)//2)
            self.update(index, diff, node*2+1, (start+end)//2+1, end)


class Fenwick:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(len(self.array)+1)]
        for i, a in enumerate(array):
            self.update(i, a)
    
    def update(self, i: int, diff: int):
        i += 1
        while i < len(self.tree):
            self.tree[i] += diff
            i += (i & -i)
    
    def _sum(self, i: int):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= (i & -i)
        return ans
    
    def sum(self, start: int, end: int):
        return self._sum(end+1) - self._sum(start)


def solution(n: int, stars: defaultdict, Tree):
    tree = Tree([0 for _ in range(400001)])
    ys = stars.keys()
    ys = sorted(ys, reverse=True)
    faces = 0

    for y in ys:
        for x in stars[y]:
            left = tree.sum(0, x-1)
            right = tree.sum(x+1, 400000)
            faces = (faces + ((left%MOD) * (right%MOD)))%MOD
        for x in stars[y]:
            tree.update(x, 1)

    return faces


def main():
    n = read_single_int()
    starts = defaultdict(lambda: [])
    for _ in range(n):
        x, y = read_list_int()
        x += 200000
        y += 200000
        starts[y].append(x)
    print(solution(n, starts, Fenwick))


if __name__ == '__main__':
    main()