from typing import List

#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_end = False


# @lc code=start
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Node('')
        curr_node = trie
        for num in arr1:
            num = str(num)
            for c in num:
                if c not in curr_node.children:
                    curr_node.children[c] = Node(c)
                curr_node = curr_node.children[c]
            curr_node.is_end = True
            curr_node = trie
        
        max_len = 0
        len = 0
        
        for num in arr2:
            curr_node = trie
            len = 0
            num = str(num)
            for c in num:
                if c not in curr_node.children:
                    max_len = max(max_len, len)
                    break
                len += 1
                curr_node = curr_node.children[c]
            else:
                max_len = max(max_len, len)
        return max_len
        
# @lc code=end

def main():
    sol = Solution()
    ans = sol.longestCommonPrefix([13, 27, 45], [22, 27, 48])
    print(ans)


if __name__ == "__main__":
    main()