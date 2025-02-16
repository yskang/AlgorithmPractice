# Title: 편광판
# Link: https://www.acmicpc.net/problem/28475

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


class SegmentTree:
    def __init__(self, array: list):
        self.array = array
        self.start = 0
        self.end = len(array) - 1
        self.tree = [[] for _ in range(len(array)*4)]  # left, pass, right
        self._init_tree(self.start, self.end, 1)  # 1 == root node

    def _init_tree(self, start: int, end: int, node: int):
        if start == end:
            index = self.array[start]
            self.tree[node] = [index, 1, index]
            return
        mid = (start + end) // 2
        self._init_tree(start, mid, node*2)
        self._init_tree(mid+1, end, node*2+1)
        left_l, left_p, left_r = self.tree[node*2]
        right_l, right_p, right_r = self.tree[node*2+1]
        self.tree[node] = [left_l, left_p & right_p & (abs(left_r - right_l) not in [2, 6]), right_r]

    def _query(self, start: int, end: int, left: int, right: int, node: int):
        if right < start or end < left:  # node is out of range
            return []
        if left <= start and end <= right:  # node is in range
            return self.tree[node]
        mid = (start + end) // 2

        left_query = self._query(start, mid, left, right, node*2)
        right_query = self._query(mid+1, end, left, right, node*2+1)

        if left_query != [] and right_query != []:
            left_l, left_p, left_r = left_query
            right_l, right_p, right_r = right_query
            return [left_l, left_p & right_p & (abs(left_r - right_l) not in [2, 6]), right_r]
        elif left_query == [] and right_query != []:
            return right_query
        elif left_query != [] and right_query == []:
            return left_query
        else:
            return []


    def _update(self, start: int, end: int, index: int, val: int, node: int):
        if start == end:
            self.tree[node][0] = val
            self.tree[node][2] = val
            return
        mid = (start + end) // 2
        if start <= index <= mid:
            self._update(start, mid, index, val, node*2)
        else:
            self._update(mid+1, end, index, val, node*2+1)
        left_l, left_p, left_r = self.tree[node*2]
        right_l, right_p, right_r = self.tree[node*2+1]
        self.tree[node] = [left_l, left_p & right_p & (abs(left_r - right_l) not in [2, 6]), right_r]

    def query(self, left: int, right: int):
        return self._query(self.start, self.end, left, right, 1)

    def update(self, index: int, val: int):
        self._update(self.start, self.end, index, val, 1)


def solution(n: int, m: int, initial_state: list, quries: list) -> str:
    seg_tree = SegmentTree(initial_state)
    for q, a, b in quries:
        if q == 1:
            seg_tree.update(a-1, b)
        else:
            print(seg_tree.query(a-1, b-1)[1])


def main():
    n, m = read_list_int()
    initial_state = read_list_int()
    quries = []
    for _ in range(m):
        quries.append(read_list_int())
    solution(n, m, initial_state, quries)


if __name__ == '__main__':
    main()
