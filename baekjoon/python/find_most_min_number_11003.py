# Title: 최솟값 찾기
# Link: https://www.acmicpc.net/problem/11003

import sys
import collections


read_list_int = lambda: sys.stdin.readline().strip().split(' ')


class Segment_Min_Tree:
    '''
    A Class used to get partial min of an array and update data
    ...
    Attributes
    ----------
    array : list
        a list which to make a segment tree

    Methods
    -------
    init(tree, start, end, node)
        make segment tree from the array. don't call this method directly.
    min(left, right, node=1, start=0, end=-1)
        return the partial min of the array.
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
        self.tree = [0 for _ in range(len(self.array) * 4)]
        self.init(self.tree, 0, len(self.array)-1, 1)
        self.last_index = len(array)-1

    def init(self, tree, start, end, node):
        '''
        Don't Call This Method Directly
        '''        
        if start == end:
            tree[node] = start
            return tree[node]
        mid = (start + end) // 2
        left = self.init(tree, start, mid, node * 2)
        right = self.init(tree, mid + 1, end, node * 2 + 1)
        if self.array[left] < self.array[right]:
            tree[node] = left
        else:
            tree[node] = right
        return tree[node]

    def min(self, left, right, node=1, start=0, end=-1):
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
            a minimum value of the part of the array. min([left, left+1, left+2 .. right-2, right-1, right])
        '''
        if end == -1:
            end = self.last_index        
        if left > end or right < start:
            return -1
        if left <= start and end <= right:
            return self.tree[node]
        left_index = self.min(left, right, node*2, start, (start+end)//2)
        right_index = self.min(left, right, node*2+1, (start+end)//2+1, end)
        if left_index == -1 and right_index == -1:
            return -1
        elif left_index == -1:
            return right_index
        elif right_index == -1:
            return left_index
        else:
            if self.array[left_index] < self.array[right_index]:
                return left_index
            return right_index


def solution_window(list_length: int, window_width: int, numbers: list):
    window = collections.deque([])
    for i, number in enumerate(numbers):
        num = int(number)
        while len(window) != 0 and window[0][1] < i-window_width+1:
            window.popleft()
        while len(window) != 0 and num <= window[-1][0]:
            window.pop()
        window.append((num, i))
        print(window[0][0], end=' ')


def solution(n: int, l: int, a: list):
    a = list(map(int, a))
    min_tree = Segment_Min_Tree(a)
    ds = []
    for end in range(n):
        ds.append(a[min_tree.min(max(0, end - l + 1), end)])
    print(' '.join(map(str, ds)))


def main():
    n, l = read_list_int()
    n, l = int(n), int(l)
    a = read_list_int()
    # solution_window(int(n), int(l), a)
    solution(n, l, a)


if __name__ == '__main__':
    main()