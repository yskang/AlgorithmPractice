# Title: minimum_number_of_changes_to_make_binary_string_beautiful
# Link: https://www.acmicpc.net/problem/beautiful


class Solution:
    def minChanges(self, s: str) -> int:
        s = list(s)
        count = 0
        while s:
            c2 = s.pop()
            c1 = s.pop()
            if c1 != c2:
                count += 1
        return count