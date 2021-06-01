# Title: 친구 네트워크
# Link: https://www.acmicpc.net/problem/4195

import sys
from collections import defaultdict

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_words = lambda: sys.stdin.readline().strip().split(' ')

class UnionFind:
    def __init__(self, n: int):
        self.sizes = [1] * n
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            self.sizes[yset] += self.sizes[xset]
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            self.sizes[xset] += self.sizes[yset]
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[yset] + 1
            self.sizes[xset] += self.sizes[yset]
    
    def get_size(self, x: int) -> int:
        return self.sizes[self.find(x)]


def main():
    t = read_single_int()
    for _ in range(t):
        number = [0]
        def set_num() -> int:
            number[0] += 1
            return number[0]
        name_to_number = defaultdict(set_num)
        f = read_single_int()
        uf = UnionFind(2*f+1)
        for _ in range(f):
            a, b = read_list_words()
            uf.union(name_to_number[a], name_to_number[b])
            print(f'{uf.get_size(name_to_number[a])}')

if __name__ == '__main__':
    main()