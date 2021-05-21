# Title: 3Sum
# Link: https://leetcode.com/problems/3sum/

from itertools import combinations
from collections import defaultdict

class Solution:
    def three_sum(self, nums: list) -> list:
        ans = []
        minus, plus = [], []
        zeros = 0
        minus_count, plus_count = [0 for _ in range(10**5+1)], [0 for _ in range(10**5+1)]
        for num in nums:
            if num < 0:
                minus_count[-num] += 1
                if minus_count[-num] == 1:
                    minus.append(-num)
            elif num > 0:
                plus_count[num] += 1
                if plus_count[num] == 1:
                    plus.append(num)
            else:
                zeros += 1

        minus = sorted(minus)
        plus = sorted(plus)

        minus_max = minus[-1] if minus else 0
        plus_max = plus[-1] if plus else 0

        if zeros >= 3:
            ans.append([0, 0, 0])
        if zeros >= 1:
            if len(plus) < len(minus):
                for p in plus:
                    if minus_count[p] >= 1:
                        ans.append([0, p, -p])
            else:
                for m in minus:
                    if plus_count[m] >= 1:
                        ans.append([0, -m, m])
        
        for a in range(len(minus)):
            minus_a = minus[a]
            if minus_a >= plus_max:
                break
            if minus_count[minus_a] >= 2 and minus_a*2 <= plus_max and  plus_count[minus_a*2] >= 1:
                ans.append([-minus_a, -minus_a, 2*minus_a])
            for b in range(a+1, len(minus)):
                minus_b = minus[b]
                if minus_a+minus_b > plus_max:
                    break
                if plus_count[minus_a+minus_b] >= 1:
                    ans.append([-minus_a, -minus_b, minus_a+minus_b])

        for a in range(len(plus)):
            plus_a = plus[a]
            if plus_a >= minus_max:
                break
            if plus_count[plus_a] >= 2 and plus_a*2 <= minus_max and minus_count[plus_a*2] >= 1:
                ans.append([-plus_a*2, plus_a, plus_a])
            for b in range(a+1, len(plus)):
                plus_b = plus[b]
                if plus_a+plus_b > minus_max:
                    break
                if minus_count[plus_a+plus_b] >= 1:
                    ans.append([plus_a, plus_b, -plus_a-plus_b])

        return ans


def main():
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.three_sum(nums))


if __name__ == '__main__':
    main()