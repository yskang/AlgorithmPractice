# Title: 인재야 머쉬맘 잡았어?
# Link: https://www.acmicpc.net/problem/17221

import sys
from collections import deque, defaultdict
from math import floor


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def attack(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    ph_mush -= attack_inje
    ph_inje -= attack_mush
    return ph_inje, attack_inje, ph_mush, attack_mush


def counterattack(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    ph_mush -= attack_mush
    ph_inje += floor(ph_inje * 0.1)
    return ph_inje, attack_inje, ph_mush, attack_mush


def buff(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    attack_inje += floor(attack_inje * 0.2)
    ph_inje -= (3 * attack_mush)
    return ph_inje, attack_inje, ph_mush, attack_mush


def solution(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    cache = defaultdict(lambda: False)
    turn = 0
    queue = deque()
    queue.append((ph_inje, attack_inje, ph_mush, attack_mush, turn))
    cache[(ph_inje, attack_inje, ph_mush, attack_mush)] = True
    while queue:
        ph_i, at_i, ph_m, at_m, t = queue.popleft()
        ph_i_b, at_i_b, ph_m_b, at_m_b = ph_i, at_i, ph_m, at_m

        ph_i, at_i, ph_m, at_m = attack(ph_i, at_i, ph_m, at_m)
        if ph_m <= 0:
            return t+1
        if ph_i > 0 and not cache[(ph_i, at_i, ph_m, at_m)]:
            cache[(ph_i, at_i, ph_m, at_m)] = True
            queue.append((ph_i, at_i, ph_m, at_m, t+1))
        
        ph_i, at_i, ph_m, at_m = ph_i_b, at_i_b, ph_m_b, at_m_b
        ph_i, at_i, ph_m, at_m = counterattack(ph_i, at_i, ph_m, at_m)
        if ph_m <= 0:
            return t+1
        if ph_i > 0 and not cache[(ph_i, at_i, ph_m, at_m)]:
            cache[(ph_i, at_i, ph_m, at_m)] = True
            queue.append((ph_i, at_i, ph_m, at_m, t+1))

        ph_i, at_i, ph_m, at_m = ph_i_b, at_i_b, ph_m_b, at_m_b
        if at_i >= 5:
            ph_i, at_i, ph_m, at_m = buff(ph_i, at_i, ph_m, at_m)
            if ph_m <= 0:
                return t+1
            if ph_i > 0 and not cache[(ph_i, at_i, ph_m, at_m)]:
                cache[(ph_i, at_i, ph_m, at_m)] = True
                queue.append((ph_i, at_i, ph_m, at_m, t+1))
        print('Turn: {}, inje ph: {}, mushmom ph: {}'.format(t, ph_i_b, ph_m_b))


def main():
    ph_inje, attack_inje, ph_mush, attack_mush = read_list_int() 
    print(solution(ph_inje, attack_inje, ph_mush, attack_mush))


if __name__ == '__main__':
    main()