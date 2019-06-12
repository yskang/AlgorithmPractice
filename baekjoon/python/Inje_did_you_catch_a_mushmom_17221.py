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
    ph_inje = floor(ph_inje * 1.1)
    return ph_inje, attack_inje, ph_mush, attack_mush


def buff(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    attack_inje = floor(attack_inje * 1.2)
    ph_inje -= (3 * attack_mush)
    return ph_inje, attack_inje, ph_mush, attack_mush


def solution(ph_inje: int, attack_inje: int, ph_mush: int, attack_mush: int):
    turn = 0

    while ph_mush > 0:
        if attack_inje <= 5:
            if 

    return turn

def main():
    ph_inje, attack_inje, ph_mush, attack_mush = read_list_int() 
    print(solution(ph_inje, attack_inje, ph_mush, attack_mush))


if __name__ == '__main__':
    main()