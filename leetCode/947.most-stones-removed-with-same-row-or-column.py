#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
from typing import List


# @lc code=start
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        return 0
        
# @lc code=end


def main():
    sol = Solution()
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    
    
    print(sol.removeStones(stones))


if __name__ == "__main__":
    main()
