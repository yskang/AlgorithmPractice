# Title: 문제제목
# Link: https://www.acmicpc.net/problem/오큰수

import sys


class Solution:
    def __init__(self):
        self.read_input()

    def solve(self):
        pass

    def read_input(self):
        pass

    def read_single_int(self):
        return int(sys.stdin.readline().strip())

    def read_list_int(self):
        return list(map(int, sys.stdin.readline().strip().split(' ')))

    def read_single_str(self) -> str:
        return sys.stdin.readline().strip()


if __name__ == '__main__':
    solution = Solution()
    solution.solve()
