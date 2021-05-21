# Title: 3Sum
# Link: https://leetcode.com/problems/3sum/

from itertools import combinations
from collections import defaultdict

class Solution:
    def threeSum(self, nums: list) -> list:
        ans = []

        nums = sorted(nums)
        prev_num = None

        for i, num in enumerate(nums):
            if num > 0:
                break
            if prev_num != num:
                prev_num = num
                left, right = i+1, len(nums)-1
                while left < right:
                    sums = num + nums[left] + nums[right]
                    if sums < 0:
                        left += 1
                    elif sums > 0:
                        right -= 1
                    else:
                        ans.append([num, nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1


        return ans


def main():
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))


if __name__ == '__main__':
    main()