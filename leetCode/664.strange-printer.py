#
# @lc app=leetcode id=664 lang=python3
#
# [664] Strange Printer
#

# @lc code=start

from collections import defaultdict


class Solution:
    def strangePrinter(self, s: str) -> int:
        self.ns = [s[0]]
        for c in s[1:]:
            if self.ns[-1] != c:
                self.ns.append(c)
        self.cache = defaultdict(lambda: -1)
        return self.get_min_prints(0, len(self.ns)-1)

    def get_min_prints(self, start, end) -> int:
        if start > end:
            return 0
        if start == end:
            return 1
        if self.cache[(start, end)] != -1:
            return self.cache[(start, end)]
        min_count = 1 + self.get_min_prints(start+1, end)
        for i in range(start+1, end+1):
            if self.ns[i] == self.ns[start]:
                min_count = min(min_count, self.get_min_prints(start, i-1) + self.get_min_prints(i+1, end))
        self.cache[(start, end)] = min_count
        return min_count

# @lc code=end


def main():
    sol = Solution()
    s = "leetcode"
    print(sol.strangePrinter(s))


if __name__ == "__main__":
    main()
