# Title: Combinations
# Link: https://leetcode.com/problems/combinations/

from typing import List

class Problem:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

def solution():
    n, k = 5, 3
    problem = Problem()
    return problem.combine(n, k)


def main():
    print(solution())


if __name__ == '__main__':
    main()