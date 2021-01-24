# Title: 3Sum
# Link: https://leetcode.com/problems/3sum/

from itertools import combinations
from collections import defaultdict

class Solution:
    def threeSum(self, nums: list) -> list:
        ans = set()
        ans_dict = set()

        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1
 
        # for all diffeerent
        x = sorted(d.keys())
        for a, b in combinations(x, 2):
            if (a, b) in ans_dict:
                continue
            d[a] -= 1
            d[b] -= 1
            if d[-a-b]:
                s = sorted([a, b, -a-b])
                ans.add(tuple(s))
                ans_dict.add((s[0], s[1]))
                ans_dict.add((s[0], s[2]))
                ans_dict.add((s[1], s[2]))
            d[a] += 1
            d[b] += 1
            
        # for two same
        for a in x:
            if d[a] >= 2:
                if a > 0:
                    t = (-a-a, a, a)
                else:
                    t = (a, a, -a-a)
            
                if t not in ans:
                    d[a] -= 2
                    if d[-a-a] > 0:
                        ans.add(t)

        return ans


def main():
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))


if __name__ == '__main__':
    main()