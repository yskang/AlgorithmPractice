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

if __name__ == "__main__":
    uf = UnionFind(10)
    print(uf.size(1))
    print(uf.size(2))
    print(uf.p)

    uf.union(1,2)
    print(uf.size(1))
    print(uf.size(2))
    print(uf.p)
    print(uf.find(1))
    print(uf.find(2))
    print(uf.find(3))
    
    uf.union(1,3)
    print(uf.size(1))
    print(uf.size(2))
    print(uf.size(3))
    print(uf.p)
    print(uf.find(1))
    print(uf.find(2))
    print(uf.find(3))