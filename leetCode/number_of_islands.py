# Title: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/

from typing import List

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

class Problem:
    def num_islands(self, grid: List[List[str]]) -> int:
        count = 0
        for y, row in enumerate(grid):
            for x, p in enumerate(row):
                if p == '1':
                    self.fill(grid, y, x)
                    count += 1
        return count
    
    def fill(self, grid: List[List[str]], y: int, x: int) -> None:
        grid[y][x] = '0'
        for dy, dx in directions:
            yy, xx = y+dy, x+dx
            if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]) and grid[yy][xx] == '1':
                self.fill(grid, yy, xx)


def solution():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    problem = Problem()
    return problem.num_islands(grid)


def main():
    print(solution())


if __name__ == '__main__':
    main()