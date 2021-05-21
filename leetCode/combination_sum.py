# Title: Combination Sum
# Link: https://leetcode.com/problems/combination-sum/

from typing import List
from collections import defaultdict, deque
from bisect import bisect_left

class Problem:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        candi_dict = defaultdict(lambda: 0)
        for i, candi in enumerate(candidates):
            candi_dict[candi] = i
        q = deque()
        q.append([])
        ans = []

        while q:
            vals =  q.popleft()
            sum_vals = sum(vals)
            start = candi_dict[vals[-1]] if vals else 0
            for idx in range(start, len(candidates)):
                new_val = vals + [candidates[idx]]
                sum_new_val = sum_vals + candidates[idx]
                if  sum_new_val == target:
                    ans.append(new_val)
                elif sum_new_val < target:
                    q.append(new_val)
                else:
                    continue
        return ans
    
        
def solution():
    candidates = [2, 3, 6, 7]
    target = 7

    problem = Problem()
    return problem.combination_sum(candidates, target)


def main():
    print(solution())


if __name__ == '__main__':
    main()