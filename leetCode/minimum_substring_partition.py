# Title: Minimum Substring Partition of Equal Character Frequency
# Link: https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
from collections import defaultdict


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        max_count = len(s)
        # dp[n] : minimum balanced count from 0 to n
        dp = [max_count for _ in range(max_count)]
        for right in range(max_count):
            char_frq = defaultdict(lambda: 0)
            for left in range(right, -1, -1):
                char_frq[s[left]] += 1
                if len(set(char_frq.values())) == 1:
                    # dp update
                    value = dp[left-1] + 1 if left > 0 else 1
                    dp[right] = min(dp[right], value)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumSubstringsInPartition("abacaba"))
    print(s.minimumSubstringsInPartition("aa"))
    print(s.minimumSubstringsInPartition("aaaa"))
    print(s.minimumSubstringsInPartition("abc"))
