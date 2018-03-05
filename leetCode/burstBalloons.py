# https://leetcode.com/problems/burst-balloons/description/
class Solution:
    def maxCoins(self, nums):
        ns = [1] + [i for i in nums if i > 0] + [1]
        n = len(ns)
        dp = [[0]*n for _ in range(n)]
        
        for width in range(2, n):
            for left_index in range(0, n-width):
                right_index = left_index+width
                for i in range(left_index+1, right_index):
                    dp[left_index][right_index] = max(dp[left_index][right_index], ns[left_index]*ns[i]*ns[right_index] + dp[left_index][i] + dp[i][right_index])
        return dp[0][n-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCoins(([3, 1, 5, 8])))

