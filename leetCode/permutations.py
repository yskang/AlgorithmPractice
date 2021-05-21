# Title: Permutations
# Link: https://leetcode.com/problems/permutations/

from typing import List


class Problem:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums.pop()]]
        new_ans = []

        while nums:
            n = nums.pop()
            for e in ans:
                for i in range(len(e)+1):
                    new_ans.append(e[:i] + [n] + e[i:])
            ans, new_ans = new_ans, []

        return ans
    
    

def solution():
    nums = [1, 2, 3, 4]
    problem = Problem()
    return problem.permute(nums)


def main():
    print(solution())


if __name__ == '__main__':
    main()