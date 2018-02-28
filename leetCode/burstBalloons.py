# https://leetcode.com/problems/burst-balloons/description/
class Solution:
    def maxCoins(self, nums):
        ns = [1] + [i for i in nums if i > 0] + [1]
        n = len(ns)
        dp = [[0]*n for _ in range(n)]

        for width in range(2, n):
            for left in range(0, n-width):
                right = left+width
                print(width, left, right)
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], ns[left]*ns[i]*ns[right] + dp[left][i] + dp[i][right])
        return dp[0][n-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxCoins(([3, 1, 5, 8])))

