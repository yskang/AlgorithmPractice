# Title: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/


from typing import List
from heapq import heappop, heappush


class Problem:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heappush(q, -num)
        for _ in range(k-1):
            heappop(q)
        return -heappop(q)


def solution():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    problem = Problem()
    return problem.find_kth_largest(nums, k)


def main():
    print(solution())


if __name__ == '__main__':
    main()