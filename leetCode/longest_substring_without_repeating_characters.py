# Title: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

class Problem:
    def length_of_longest_substring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        included = defaultdict(lambda: -1)
        left, right = 0, 1
        included[s[left]] = 0
        current_max = 1
        while True:
            if included[s[right]] == -1 or included[s[right]] < left:
                included[s[right]] = right
                current_max = max(current_max, right-left+1)
                right += 1
            else:
                left = included[s[right]] + 1
                included[s[right]] = right
                right += 1
                if len(s)-left <= current_max:
                    break
            
            if right >= len(s):
                break

        return current_max


def solution():
    s = "abcabcbb"
    problem = Problem()
    return problem.length_of_longest_substring(s)


def main():
    print(solution())


if __name__ == '__main__':
    main()