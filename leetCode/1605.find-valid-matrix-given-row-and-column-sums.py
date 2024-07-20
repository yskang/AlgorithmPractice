#
# @lc app=leetcode id=1605 lang=python3
#
# [1605] Find Valid Matrix Given Row and Column Sums
#
from typing import List


# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                ans[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ans[i][j]       
                colSum[j] -= ans[i][j]
        return ans
    
# @lc code=end

def main():
    sol = Solution()
    row = [3, 8]
    col = [4, 7]
    print(sol.restoreMatrix(row, col))


if __name__ == "__main__":
    main()
