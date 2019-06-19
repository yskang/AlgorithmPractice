# Title: 인재야 머쉬맘 잡았어?
# Link: https://www.acmicpc.net/problem/17221

import sys
from collections import deque, defaultdict
from math import floor, ceil
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(init_data: SimpleNamespace):
    min_turn = 99999999999

    if init_data.inje.attack < 5:
        # counter attack and attack. no buff
        ph_inje = init_data.inje.ph
        ph_mush = init_data.mush_mom.ph
        attack_inje = init_data.inje.attack
        attack_mush = init_data.mush_mom.attack

        c = 0
        while True:
            a = ceil(ph_mush/attack_inje)
            if ph_inje >= a*attack_mush and  a+c < min_turn:
                min_turn = a+c

            if ph_mush <= 0:
                break

            if ph_inje > 999999999:
                break

            c += 1
            ph_inje = floor(ph_inje*1.1)
            ph_mush -= attack_mush

    else:
        counterattack_limit = ceil(init_data.mush_mom.ph / init_data.mush_mom.attack)
        for c in range(0, counterattack_limit+1):
            # counter attack, increase ph of inje, decrease ph of mush_mom
            # there is no change to dead of inje

            ph_inje = init_data.inje.ph
            ph_mush = init_data.mush_mom.ph
            attack_inje = init_data.inje.attack
            attack_mush = init_data.mush_mom.attack

            for _ in range(c):
                ph_inje = floor(ph_inje*1.1)
                ph_mush -= attack_mush
                if ph_mush <= 0 and c < min_turn:
                    min_turn = c
                    break
           
            if ph_mush <= 0:
                # kill mushmom by counterattack only
                continue

            b = 0
            # Buff, decrease ph of inje as 3 times of attack of mush, increase 1.2 times of attack of inje.
            while True:
                a = ceil(ph_mush/attack_inje)
                if ph_inje >= a*attack_mush and a+b+c < min_turn:
                    min_turn = a+b+c
                if attack_inje >= ph_mush:
                    break
                if ph_inje <= 0:
                    break

                b += 1
                ph_inje -= (3*attack_mush)
                attack_inje = floor(attack_inje*1.2)

    return min_turn


def main():
    ph_inje, attack_inje, ph_mush, attack_mush = read_list_int() 
    init_data = SimpleNamespace(inje=SimpleNamespace(ph = ph_inje, attack = attack_inje), mush_mom=SimpleNamespace(ph = ph_mush, attack = attack_mush))
    print(solution(init_data))


if __name__ == '__main__':
    main()
