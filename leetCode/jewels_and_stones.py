# Title: Jewels and Stones
# Link: https://leetcode.com/problems/jewels-and-stones/

from collections import defaultdict

class Problem:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        count = 0
        stone_map = defaultdict(lambda: 0)
        for stone in stones:
            stone_map[stone] += 1

        for jewel in jewels:
            count += stone_map[jewel]

        return count


def solution():
    jewels = 'z'
    stones = 'ZZ'

    problem = Problem()
    return problem.num_jewels_in_stones(jewels, stones)


def main():
    print(solution())


if __name__ == '__main__':
    main()