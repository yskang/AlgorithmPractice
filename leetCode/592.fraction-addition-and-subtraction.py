#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#

import math


# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("-", " -").replace("+", " +")
        expression = expression.split()
        bases = []
        all_trems = []
        res = 0
        for term in expression:
            term = term.split("/")
            all_trems.append((int(term[0]), int(term[1])))
            bases.append(int(term[1]))
        new_base = math.lcm(*bases)
        for child, base in all_trems:
            child *= new_base // base
            res += child
        cd = math.gcd(res, new_base)
        return f'{res//cd}/{new_base//cd}'
# @lc code=end


def main():
    sol = Solution()
    expression = "-1/2+1/2"
    print(sol.fractionAddition(expression))

    expression = "-1/2+1/2+1/3"
    print(sol.fractionAddition(expression))

    expression = "1/3-1/2"
    print(sol.fractionAddition(expression))


if __name__ == "__main__":
    main()
