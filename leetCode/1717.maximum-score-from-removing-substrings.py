#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#

# @lc code=start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        self.s = s
        pairs = ['ab', 'ba'] if x > y else ['ba', 'ab']
        score += self.remove_pair(pairs[0]) * max(x, y)
        score += self.remove_pair(pairs[1]) * min(x, y)
        return score

    def remove_pair(self, pair: str) -> int:
        count = 0
        stack = []
        for c in self.s:
            stack.append(c)
            if len(stack) >= 2 and stack[-2] == pair[0] and stack[-1] == pair[1]:
                stack.pop()
                stack.pop()
                count += 1
        self.s = ''.join(stack)
        return count
        
# @lc code=end

