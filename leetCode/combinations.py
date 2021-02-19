# Title: Combinations
# Link: https://leetcode.com/problems/combinations/

from typing import List


class Problem:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return list(map(lambda e: [e], [i for i in range(1, n+1)]))
        ans = []
        for e in range(n, 1, -1):
            for f in self.combine(e-1, k-1):
                ans.append([e] + f)
        return ans

def solution():
    n, k = 5, 3
    problem = Problem()
    return problem.combine(n, k)


def main():
    print(solution())


if __name__ == '__main__':
    main()