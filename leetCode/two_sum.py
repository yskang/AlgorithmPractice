# Title: two sum
# Link: https://leetcode.com/problems/two-sum/

import sys


sys.setrecursionlimit(10 ** 6)


class Solution:
    def two_sum_two_pointer(self, nums, target):
        nums_zip = zip(nums, [i for i in range(len(nums))])
        nums_zip = sorted(nums_zip, key=lambda x: x[0])
        left, right = 0, len(nums)-1
        while left < right:
            s = nums_zip[left][0] + nums_zip[right][0]
            if s < target:
                left += 1
            elif target < s:
                right -= 1
            else:
                return list(sorted([nums_zip[left][1], nums_zip[right][1]]))
        return 0

    def two_sum(self, nums, target):
        for i, a in enumerate(nums):
            for j in range(len(nums)-1, i, -1):
                if a + nums[j] == target:
                    return [i, j]


def solution():
    nums = [3, 2, 4]
    target = 6
    sol = Solution()
    return sol.two_sum(nums, target)


def main():
    print(solution())


if __name__ == '__main__':
    main()