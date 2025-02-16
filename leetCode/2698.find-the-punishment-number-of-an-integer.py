#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#

from collections import defaultdict

# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        punish_nums = []
        cache = defaultdict(lambda: False)
        for i in range(1, n+1):
            if self.is_punish_num(i, cache):
                punish_nums.append(i*i)
        return sum(punish_nums)

    def is_punish_num(self, n: int, cache: defaultdict) -> bool:
        n_sqr = n*n
        if n in self.all_seperate(n_sqr, cache):
            return True
        return False

    def all_seperate(self, n: int, cache: defaultdict) -> set:
        if n in cache:
            return cache[n]
        ret = set()
        if 0 <= n < 10:
            ret.add(n)
            cache[n] = ret
            return ret
        n_str = str(n)
        total = set()
        total.add(n)
        for i in range(1, len(n_str)):
            left, right = n_str[:i], n_str[i:]
            left = self.all_seperate(int(left), cache)
            right = self.all_seperate(int(right), cache)
            for l in left:
                for r in right:
                    total.add(l+r)
        cache[n] = total
        return total


# @lc code=end

def main():
    sol = Solution()
    print(sol.punishmentNumber(37))


if __name__ == "__main__":
    main()
