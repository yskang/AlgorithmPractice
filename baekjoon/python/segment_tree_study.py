import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class SegmentTree:
    def __init__(self, nums: list):
        self.nums = nums
        self.tree = [0 for _ in range(len(nums)*2+2)]
        self._init(1, 0, len(nums)-1)
    
    def _init(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.nums[start]
            return self.nums[start]
        else:
            self.tree[node] = self._init(node*2, start, (start+end)//2) + self._init(node*2+1, (start+end)//2+1, end)
            return self.tree[node]

    def update(self, node: int, start: int, end: int, index: int, diff: int):
        if index < start or end < index:
            return



def solution(ns):
    segment_tree = SegmentTree(ns)
    print(segment_tree.tree)


def main():
    ns = read_list_int()
    print(solution(ns))


if __name__ == '__main__':
    main()