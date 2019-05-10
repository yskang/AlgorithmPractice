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

if __name__ == "__main__":
    fenwick = Fenwick([1,2,3,4,5,6,7,8,9,10])
    print(fenwick.sum(0,9))