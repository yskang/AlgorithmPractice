# Title: Minimum Height Trees
# Link: https://leetcode.com/problems/minimum-height-trees/


from typing import List
from collections import defaultdict

class Problem:
    def __init__(self) -> None:
        self.graph = defaultdict(lambda: set())

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)

        leaves = []
        for node in self.graph:
            if len(self.graph[node]) == 1:
                leaves.append(node)

        next_leaves = set()
        while len(self.graph) > 2:
            for leaf in leaves:
                target = self.graph[leaf].pop()

                del self.graph[leaf]
                self.graph[target].discard(leaf)
                next_leaves.add(target)
            temp = []
            for leaf in next_leaves:
                if len(self.graph[leaf]) == 1:
                    temp.append(leaf)
            leaves, next_leaves = temp, set()

        return list(self.graph.keys())


def solution():
    n = 8
    edges = [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]

    problem = Problem()
    return problem.findMinHeightTrees(n, edges)


def main():
    print(solution())


if __name__ == '__main__':
    main()