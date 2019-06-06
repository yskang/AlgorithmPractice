# Title: 인재야 머쉬맘 잡았어?
# Link: https://www.acmicpc.net/problem/17221

import sys
from collections import deque
from math import floor


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    turn = 0
    queue = deque()
    queue.append((ph_inje, attack_inje, ph_mush, attack_mush, turn))

    while queue:
        inje_ph, inje_attack, mush_ph, mush_attack, turn = queue.popleft()
        inje_ph_t, inje_attack_t, mush_ph_t, mush_attack_t = inje_ph, inje_attack, mush_ph, mush_attack

        # attack
        mush_ph -= inje_attack
        inje_ph -= mush_attack

        if mush_ph <= 0:
            return turn+1
        
        if inje_ph > 0:
            queue.append((inje_ph, inje_attack, mush_ph, mush_attack, turn+1))

        # revenge
        inje_ph, inje_attack, mush_ph, mush_attack = inje_ph_t, inje_attack_t, mush_ph_t, mush_attack_t
        inje_ph += floor(inje_ph * 0.1)
        mush_ph -= mush_attack

        if mush_ph <= 0:
            return turn+1
        
        if inje_ph > 0:
            queue.append((inje_ph, inje_attack, mush_ph, mush_attack, turn+1))

        # buff
        inje_ph, inje_attack, mush_ph, mush_attack = inje_ph_t, inje_attack_t, mush_ph_t, mush_attack_t
        inje_attack += floor(inje_attack * 0.2)
        inje_ph -= (mush_attack * 3)

        if mush_ph <= 0:
            return turn+1
        
        if inje_ph > 0:        
            queue.append((inje_ph, inje_attack, mush_ph, mush_attack, turn+1))


def main():
    ph_inje, attack_inje, ph_mush, attack_mush = read_list_int() 
    print(solution(ph_inje, attack_inje, ph_mush, attack_mush))


if __name__ == '__main__':
    main()