# Title: 토너먼트
# Link: https://www.acmicpc.net/problem/1057

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def sim_round(N, jimin, hansu):
    current_round = [False for _ in range(N)]
    current_round[jimin - 1] = True
    current_round[hansu - 1] = True
    count = 1
    while True:
        next_round = []
        for num in range(0, len(current_round), 2):
            if num + 1 >= len(current_round):
                next_round.append(current_round[num])
                break
            if not(current_round[num] | current_round[num + 1]):
                next_round.append(False)
            elif current_round[num] ^ current_round[num + 1]:
                next_round.append(True)
            else:
                return count

        current_round = next_round
        count += 1


if __name__ == '__main__':
    N, jimin, hansu = read_list_int()
    print(sim_round(N, jimin, hansu))
