# Title: Remove Duplicate Letters
# Link: https://leetcode.com/problems/remove-duplicate-letters/

import sys
from collections import defaultdict, deque
from sys import maxsize
INT_MIN = -maxsize

class SegmentTreeMax:
    def __init__(self, a: list) -> None:
        self.a = a
        self.n = len(a)
        self.segtree = [0] * (2 * self.n)
        self.construct_segment_tree(self.a, self.n)

    def construct_segment_tree(self, a: list, n: int):
        for i in range(n):
            self.segtree[n + i] = a[i]
        for i in range(n - 1, 0, -1):
            self.segtree[i] = max(self.segtree[2 * i], self.segtree[2 * i + 1])

    def update(self, pos: int, value: int):
        pos += self.n
        self.segtree[pos] = value
        while pos > 1:
            pos //= 2
            self.segtree[pos] = max(self.segtree[2 * pos], self.segtree[2 * pos + 1])

    def range_query(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        ma = INT_MIN
        while left < right:
            if left & 1:
                ma = max(ma, self.segtree[left])
                left += 1
            if right & 1:
                right -= 1
                ma = max(ma, self.segtree[right])
            left //= 2
            right //= 2
        return ma


class Problem:
    def remove_duplicate_letters(self, s: str) -> str:
        ZERO = 0
        ans = [ZERO for _ in range(len(s))]

        seg_max = SegmentTreeMax(ans)

        letter_pos = defaultdict(lambda: deque())
        for pos, c in enumerate(s):
            letter_pos[c].append(pos)

        for c in letter_pos:
            if len(letter_pos[c]) == 1:
                ans[letter_pos[c][0]] = ord(c)
                seg_max.update(letter_pos[c][0], ord(c))
        
        for c in range(ord('a'), ord('z')+1):
            c = chr(c)
            if len(letter_pos[c]) > 1:
                while letter_pos[c]:
                    i = letter_pos[c].popleft()
                    if ord(c) < seg_max.range_query(i+1, len(s)-1):
                        ans[i] = ord(c)
                        seg_max.update(i, ord(c))
                        break
        print(ans)




def solution():
    # s = 'bcabc'
    s = 'cbacdcbc'
    problem = Problem()
    return problem.remove_duplicate_letters(s)


def main():
    print(solution())


if __name__ == '__main__':
    main()