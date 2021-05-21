# Title: Trapping Rain Water
# Link: https://leetcode.com/problems/trapping-rain-water/

import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 6)


class Solution():
    def trap(self, heights: list) -> int:
        water = 0
        walls = []

        for i, height in enumerate(heights):
            last_level = 0

            while walls:
                left_height, left_index = heappop(walls)
                if left_height <= height:
                    water += (i - left_index - 1) * (left_height - last_level)
                    last_level = left_height
                else:
                    water += (i - left_index - 1) * (height - last_level)
                    heappush(walls, (left_height, left_index))
                    break

            heappush(walls, (height, i))

        return water


def main():
    solution = Solution()
    height = [4,2,0,3,2,5]

    print(solution.trap(height))


if __name__ == '__main__':
    main()