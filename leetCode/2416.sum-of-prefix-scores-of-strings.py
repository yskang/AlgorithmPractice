from typing import List
#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#


class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.count = 0


# @lc code=start
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Node('Root')

        for word in words:
            current_node = trie
            for letter in word:
                if letter not in current_node.children:
                    current_node.children[letter] = Node(letter)
                current_node = current_node.children[letter]
                current_node.count += 1

        ans = []
        for word in words:
            current_node = trie
            score = 0
            for letter in word:
                current_node = current_node.children[letter]
                score += current_node.count
            ans.append(score)

        return ans

# @lc code=end


def main():
    sol = Solution()
    ans = sol.sumPrefixScores(["abc", "ab", "bc", "b"])
    print(ans)


if __name__ == "__main__":
    main()
