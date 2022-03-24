# Title: BAZE RUNNER
# Link: https://www.acmicpc.net/problem/16720

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()


def solution(n: int, walls: list):
    moves = {'0111': [0, 1, 2, 1],
            '1011': [1, 0, 1, 2],
            '1101': [2, 1, 0, 1],
            '1110': [1, 2, 1, 0]}

    move_sum = [0, 0, 0, 0]

    for wall in walls:
        for pos, count in enumerate(moves[wall]):
            move_sum[pos] += count

    return min(move_sum) + 4 + n-2


def main():
    n = read_single_int()
    walls = []
    for _ in range(n-2):
        walls.append(read_single_str())
    print(solution(n, walls))


if __name__ == '__main__':
    main()