# Title: Palindrome Pairs
# Link: https://leetcode.com/problems/palindrome-pairs/

from typing import List


class Problem:
    def palindrome_pairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        r_words = []
        for word in words:
            r_words.append(word[::-1])
        a = '1'
        a.partition
        for i, word in enumerate(words):
            for j, r_word in enumerate(r_words):
                if i == j:
                    continue
                if word == '':
                    if r_word == words[j]:
                        ans.append((i, j))
                    continue
                elif r_word == '':
                    if word == r_words[i]:
                        ans.append((i, j))
                    continue
                elif len(word) <= len(r_word):
                    parts = r_word.partition(word)
                else:
                    parts = word.partition(r_word)
                if parts[0] == '' and parts[2] == parts[2][::-1]:
                    ans.append((i, j))
        return ans


def solution():
    words = ["a","abc","aba",""]

    problem = Problem()
    return problem.palindrome_pairs(words)


def main():
    print(solution())


if __name__ == '__main__':
    main()