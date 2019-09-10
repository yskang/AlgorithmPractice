from copy import deepcopy

class MaxSegment:
    def __init__(self, ns: list, n: int):
        self.n = n
        self.tree = [0 for _ in range(n)] + deepcopy(ns) + [0]
        for i in range(n-1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
    
    def update(self, pos: int, value: int): # value is not a diff
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos+1])

    def range_query(self, left: int, right: int):
        left += self.n
        right += 1
        right += self.n
        ma = -(10**10)
        while left < right:
            if left & 1 != 0:
                ma = max(ma, self.tree[left])
                left += 1
            if right & 1 != 0:
                right -= 1
                ma = max(ma, self.tree[right])
            left //= 2
            right //= 2
        return ma

if __name__ == "__main__":
    tree = MaxSegment([1,2,3,4,5,6,7], 7)
    print(tree.range_query(0, 0))
    print(tree.range_query(1, 1))
    print(tree.range_query(0, 6))

    print('update')
    tree.update(0, 5)
    print(tree.range_query(0, 0))
    print(tree.range_query(1, 1))
    print(tree.range_query(0, 4))
    print(tree.range_query(0, 6))
