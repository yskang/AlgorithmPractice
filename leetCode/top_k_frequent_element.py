# Title: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import defaultdict, Counter
from heapq import heappush, heappop

class Problem:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(
            lambda e: e[0], 
            sorted(
                map(lambda e: [e, nums.count(e)], set(nums))
                , key=lambda e: e[1]
                , reverse=True)[:k]))
    
    def top_k_frequent_2(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda e: e[0] ,sorted(Counter(nums).items(), key=lambda e: e[1], reverse=True)[:k]))
    
    def top_k_frequent_3(self, nums: List[int], k: int) -> List[int]:
        q = []
        dic = defaultdict(lambda: 0)
        for n in nums:
            dic[n] -= 1
            heappush(q, [dic[n], n])
        ans = []
        ans_set = set()
        while q:
            _, n = heappop(q)
            if n not in ans_set:
                ans_set.add(n)
                ans.append(n)
                if len(ans) == k:
                    break
        return ans

def solution():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    problem = Problem()
    return problem.top_k_frequent_3(nums, k)


def main():
    print(solution())


if __name__ == '__main__':
    main()