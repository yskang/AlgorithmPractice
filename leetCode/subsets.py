# Title: Subsets
# Link: https://leetcode.com/problems/subsets/

from typing import List
from functools import reduce

class Problem:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda subsets, n: subsets + [s+[n] for s in subsets], nums, [[]])


def solution():
    nums = [2, 3, 1]
    problem = Problem()
    return problem.subsets(nums)


def main():
    print(solution())


if __name__ == '__main__':
    main()