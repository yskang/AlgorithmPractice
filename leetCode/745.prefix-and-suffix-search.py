#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
from collections import defaultdict
from typing import List


INDDEX = 'index'


def trie():
    return defaultdict(trie)


class WordFilter:   
    def __init__(self, words: List[str]):
        self.trie1 = trie()
        self.trie2 = trie()
        for index, word in enumerate(words):
            current_trie = self.trie1
            self.add_index(current_trie, index)
            for letter in word:
                current_trie = current_trie[letter]
                self.add_index(current_trie, index)

            current_trie = self.trie2
            self.add_index(current_trie, index)
            for letter in word[::-1]:
                current_trie = current_trie[letter]
                self.add_index(current_trie, index)

    def add_index(self, node, idx):
        if INDDEX not in node:
            node[INDDEX] = {idx}
        else:
            node[INDDEX].add(idx)

    def f(self, pref: str, suff: str) -> int:
        cur1 = self.trie1
        for letter in pref:
            if letter not in cur1:
                return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suff[::-1]:
            if letter not in cur2: 
                return -1
            cur2 = cur2[letter]

        return max(cur1[INDDEX] & cur2[INDDEX], default=-1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end

def main():
    word_filter = WordFilter(["bananaa", "ban", "banda"])
    print(word_filter.f("a", "e"))


if __name__ == '__main__':
    main()

