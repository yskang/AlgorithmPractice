#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 2*32

        left, right = -2**31, 2**31
        while left < right:
            mid = (left + right) // 2
            ans = mid * divisor
            if ans == dividend:
                break
            elif ans < dividend:
                left = mid + 1
            else:
                right = mid
        return min(max(-2**31, mid), 2**31-1)
        
# @lc code=end

