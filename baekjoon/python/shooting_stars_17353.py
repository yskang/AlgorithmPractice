# Title: 하늘에서 떨어지는 별
# Link: https://www.acmicpc.net/problem/17353

import sys
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Segment_Tree:
    '''
    A Class used to get partial sum of an array and update data
    ...
    Attributes
    ----------
    array : list
        a list which to make a segment tree

    Methods
    -------
    init(tree, start, end, node)
        make segment tree from the array. don't call this method directly.
    sum(left, right, node=1, start=0, end=-1)
        return the partial sum of the array.
    update(index, diff, node=1, start=0, end=-1)
        update the value of the index of array as +diff.
    '''

    def __init__(self, array):
        '''
        Parameters
        ----------
        array : list
            the array that you want to make tree
        '''
        self.array = array
        self.tree = [SimpleNamespace(value=0, lazy=0) for _ in range(len(self.array) * 4)]
        self.init(self.tree, 0, len(self.array)-1, 1)
        self.last_index = len(array)-1

    def init(self, tree, start, end, node):
        '''
        Don't Call This Method Directly
        '''        
        if start == end:
            tree[node].value = self.array[start]
            return tree[node].value
        mid = (start + end) // 2
        tree[node].value = self.init(tree, start, mid, node * 2) + self.init(tree, mid + 1, end, node * 2 + 1)
        return tree[node].value

    def sum(self, left, right, node=1, start=0, end=-1):
        '''
        Parameters
        ----------
        left : int
            start index of the part [left, left+1, left+2 .. right-2, right-1, right]
        right : int
            end index of the part [left, left+1, left+2 .. right-2, right-1, right]
        
        Returns
        -------
        int
            a sum of the part of the array. sum([left, left+1, left+2 .. right-2, right-1, right])
        '''
        if end == -1:
            end = self.last_index
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node].value
        return self.sum(left, right, node*2, start, (start+end)//2) + self.sum(left, right, node*2+1, (start+end)//2+1, end)

    def lazy_sum(self, left, right, node=1, start=0, end=-1):
        if end == -1:
            end = self.last_index

        if self.tree[node].lazy != 0:
            self.tree[node].value += (end-start+1)*self.tree[node].lazy
            if start != end:
                self.tree[node*2].lazy += self.tree[node].lazy
                self.tree[node*2+1].lazy += self.tree[node].lazy
            self.tree[node].lazy = 0

        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node].value
        return self.lazy_sum(left, right, node*2, start, (start+end)//2) + self.lazy_sum(left, right, node*2+1, (start+end)//2+1, end)

    def update(self, index, diff, node=1, start=0, end=-1):
        '''
        Parameters
        ----------
        index: int
            the index of array. which you want to update value
        diff: int
            the amount of value which you wnat to add. if you want to make 4 to 10, put diff to 6
        '''

        if end == -1:
            end = self.last_index
        if not(start <= index <= end):
            return
        self.tree[node].value += diff
        if start != end:
            self.update(index, diff, node*2, start, (start+end)//2)
            self.update(index, diff, node*2+1, (start+end)//2+1, end)

    def update_range(self, diff, left, right, node=1, start=0, end=-1):
        if end == -1:
            end = self.last_index
        
        if self.tree[node].lazy != 0:
            self.tree[node].value += (end-start+1)*self.tree[node].lazy
            if start != end:
                self.tree[node*2].lazy += self.tree[node].lazy
                self.tree[node*2+1].lazy += self.tree[node].lazy
            self.tree[node].lazy = 0

        if right < start or end < left:
            return
        
        if left <= start and end <= right:
            self.tree[node].value += (end-start+1)*diff
            if start != end:
                self.tree[node*2].lazy += diff
                self.tree[node*2+1].lazy += diff
            return
        
        self.update_range(diff, left, right, node*2, start, (start+end)//2)
        self.update_range(diff, left, right, node*2+1, (start+end)//2+1, end)

        self.tree[node].value = self.tree[node*2].value + self.tree[node*2+1].value


class BinaryIndexTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0 for _ in range(n+1)]
    
    def _update(self, p: int, v: int):
        while p <= self.n:
            self.tree[p] += v
            p += (p & (-p))
    
    def update_range(self, start: int, end: int, value: int):
        self._update(start, value)
        self._update(end+1, -value)
    
    def query(self, p: int):
        s = 0
        while p > 0:
            s += self.tree[p]
            p -= (p & (-p))
        return s


def solution(n: int, ns: list, q: int, qs: list):
    bit_count = BinaryIndexTree(n)
    bit_starts = BinaryIndexTree(n)

    for query in qs:
        if query[0] == 1:
            bit_count.update_range(query[1], query[2], 1)
            bit_starts.update_range(query[1], query[2], query[1]-1)
        else:
            ans = ns[query[1]-1]
            count = bit_count.query(query[1])
            starts = bit_starts.query(query[1])
            print(ans + count * query[1] - (starts))


def solution_with_segment_tree(n: int, ns: list, q: int, qs: list):
    bit_count = Segment_Tree([0 for _ in range(n+1)])
    bit_starts = Segment_Tree([0 for _ in range(n+1)])

    for query in qs:
        if query[0] == 1:
            bit_count.update_range(1, query[1], query[2])
            bit_starts.update_range(query[1]-1, query[1], query[2])
        else:
            ans = ns[query[1]-1]
            count = bit_count.lazy_sum(query[1], query[1])
            starts = bit_starts.lazy_sum(query[1], query[1])
            print(ans + count * query[1] - (starts))


def main():
    n = read_single_int()
    ns = read_list_int()
    q = read_single_int()
    qs = []
    for _ in range(q):
        qs.append(read_list_int())
    solution_with_segment_tree(n, ns, q, qs)


if __name__ == '__main__':
    main()