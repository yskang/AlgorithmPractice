# Title: 인재야 머쉬맘 잡았어?
# Link: https://www.acmicpc.net/problem/17221

import sys
from collections import deque, defaultdict
from math import floor, ceil
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(init_data: SimpleNamespace):
    min_turn = 100001

    # cache_attack = [init_data.inje.attack]

    # if init_data.inje.attack >= 5:
    #     while True:
    #         if cache_attack[-1] >= init_data.mush_mom.ph:
    #             break
    #         cache_attack.append(floor(cache_attack[-1]*1.2))

    _ph_inje = init_data.inje.ph
    _ph_mush = init_data.mush_mom.ph
    for c in range(100001):
        if c >= min_turn:
            break
        ph_mush = init_data.mush_mom.ph
        attack_inje = init_data.inje.attack
        attack_mush = init_data.mush_mom.attack

        ph_inje = _ph_inje
        ph_mush = _ph_mush

        if ph_mush <= 0:
            if c < min_turn:
                min_turn = c
            continue
        if _ph_inje < attack_mush * floor( ph_mush / attack_inje ):
            pass
        else:
            if attack_inje > 5:
                for b in range(min_turn-c):
                    # attack_inje = cache_attack[min(b, len(cache_attack)-1)]
                    if b+c >= min_turn:
                        break

                    if ph_inje < 0:
                        break

                    a = ceil(ph_mush/attack_inje)

                    if a+b+c < min_turn:
                        if ph_inje - (a-1)*attack_mush > 0:
                            min_turn = a+b+c
                    ph_inje -= (3*attack_mush)
                    attack_inje = floor(attack_inje*1.2) #cache_attack[b]

            else:
                a = ceil(ph_mush/attack_inje)
                if a+c < min_turn:
                    if ph_inje - (a-1)*attack_mush > 0:
                        min_turn = a+c

        if _ph_inje*1.1 != float('inf'):
            _ph_inje = floor(_ph_inje*1.1)
        _ph_mush -= attack_mush

    return min_turn


def main():
    ph_inje, attack_inje, ph_mush, attack_mush = read_list_int() 
    init_data = SimpleNamespace(inje=SimpleNamespace(ph = ph_inje, attack = attack_inje), mush_mom=SimpleNamespace(ph = ph_mush, attack = attack_mush))
    print(solution(init_data))


if __name__ == '__main__':
    main()
