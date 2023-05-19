# Title: 보스몬스터 전리품
# Link: https://www.acmicpc.net/problem/20005

import sys
from collections import defaultdict, deque


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_str() -> str:
    return sys.stdin.readline().strip()


# y, x
pos_offsets = [[-1, 0], [1, 0], [0, 1], [0, -1]]  # up, down, right, left


def solution(m: int, n: int, dungeon: list, dsps: defaultdict, boss_hp: int) -> int:
    boss_pos = None
    attckings = []
    for i, line in enumerate(dungeon):
        for idx, c in enumerate(line):
            if c == 'B':
                boss_pos = [i, idx]
                break
        if boss_pos:
            break

    q = deque()
    q.append((boss_pos, 0))

    last_turn = 0

    while q:
        pos, turn = q.popleft()

        if turn > last_turn:
            last_turn = turn
            for player in attckings:
                boss_hp -= dsps[player]
                if boss_hp <= 0:
                    return len(attckings)

        y, x = pos
        for y_offset, x_offset in pos_offsets:
            new_y, new_x = y+y_offset, x+x_offset
            if 0 <= new_y < m and 0 <= new_x < n:
                if dungeon[new_y][new_x] == '.':
                    dungeon[new_y][new_x] = 'B'
                    q.append(([new_y, new_x], turn+1))
                elif 'a' <= dungeon[new_y][new_x] <= 'z':
                    attckings.append(dungeon[new_y][new_x])
                    q.append(([new_y, new_x], turn+1))
                    dungeon[new_y][new_x] = 'B'

    return len(dsps)


def main():
    m, n, p = read_list_int()
    dungeon = []
    for _ in range(m):
        dungeon.append(list(read_single_str()))
    players = defaultdict(lambda: 0)
    for _ in range(p):
        player, damage = read_single_str().split(' ')
        players[player] = int(damage)
    boss_hp = read_list_int()[0]
    print(solution(m, n, dungeon, players, boss_hp))


if __name__ == '__main__':
    main()
