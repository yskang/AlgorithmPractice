# Title: 공 넣기
# Link: https://www.acmicpc.net/problem/10810

import sys


class Solution:
    def __init__(self):
        self.read_input()

    def solve(self):
        basket = [0 for _ in range(self.n)]
        for i, j, k in self.balls:
            for idx in range(i-1, j):
                basket[idx] = k
        print(' '.join(map(str, basket)))

    def read_input(self):
        self.n, self.m = self.read_list_int()
        self.balls = []
        for _ in range(self.m):
            self.balls.append(self.read_list_int())

    def read_single_int(self):
        return int(sys.stdin.readline().strip())

    def read_list_int(self):
        return list(map(int, sys.stdin.readline().strip().split(' ')))

    def read_single_str(self) -> str:
        return sys.stdin.readline().strip()


if __name__ == '__main__':
    solution = Solution()
    solution.solve()