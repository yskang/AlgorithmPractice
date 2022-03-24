# Title: 카드
# Link: https://www.acmicpc.net/problem/11652

import sys
import collections

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(cards: list):
    nums = collections.defaultdict(lambda: 0)
    for card in cards:
        nums[card] += 1

    cs = [(nums[number], number) for number in nums]

    cs = sorted(cs, key=lambda x: (-x[0], x[1]))
    return cs[0][1]


def main():
    N = read_single_int()
    cards = []
    for _ in range(N):
        cards.append(read_single_int())
    print(solution(cards))


if __name__ == '__main__':
    main()