# Title: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/

import math

class Solution:
    def product_except_self(self, nums: list) -> list:
        ans = []
        zero_count = nums.count(0)
        if zero_count == 0:
            all_prod = math.prod(nums)
            for num in nums:
                ans.append(all_prod // num)
        elif zero_count == 1:
            all_prod = math.prod(filter(lambda x: x != 0, nums))
            for num in nums:
                ans.append(all_prod if num == 0 else 0)
        else:
            return [0 for _ in range(len(nums))]
        return ans


def problem():
    nums = [1, 0]
    solution = Solution()
    return solution.product_except_self(nums)


def main():
    print(problem())


if __name__ == '__main__':
    main()