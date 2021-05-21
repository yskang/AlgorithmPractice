# Python Program to implement
# iterative segment tree.

from sys import maxsize
INT_MAX = maxsize

class SegmentTreeMin:
    def __init__(self, a: list) -> None:
        self.a = a
        self.n = len(a)
        self.segtree = [0] * (2 * self.n)
        self.construct_segment_tree(self.a, self.n)

    def construct_segment_tree(self, a: list, n: int):
        for i in range(n):
            self.segtree[n + i] = a[i]
        for i in range(n - 1, 0, -1):
            self.segtree[i] = min(self.segtree[2 * i], self.segtree[2 * i + 1])

    def update(self, pos: int, value: int):
        pos += self.n
        self.segtree[pos] = value
        while pos > 1:
            pos //= 2
            self.segtree[pos] = min(self.segtree[2 * pos], self.segtree[2 * pos + 1])

    def range_query(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        ma = INT_MAX
        while left < right:
            if left & 1:
                ma = min(ma, self.segtree[left])
                left += 1
            if right & 1:
                right -= 1
                ma = min(ma, self.segtree[right])
            left //= 2
            right //= 2
        return ma


if __name__ == "__main__":
    a = [2, 6, 10, 4, 7, 28, 9, 11, 1, 33]

    segment_tree = SegmentTreeMin(a)
    print(segment_tree.range_query(0, 9))
    segment_tree.update(0, 0)
    print(segment_tree.range_query(0, 9))
    segment_tree.update(0, 100)
    segment_tree.update(8, 200)
    print(segment_tree.range_query(0, 9))
