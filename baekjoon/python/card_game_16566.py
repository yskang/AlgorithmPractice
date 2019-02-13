# Title: 카드 게임
# Link: https://www.acmicpc.net/problem/16566

import bisect
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, m: int, k: int, minsu: list, chulsu: list):
    minsu = sorted(minsu)
    next_card = defaultdict(lambda: -1)
    prev = minsu[0]
    for card in minsu[1:]:
        next_card[prev] = card
        prev = card

    ans = []
    for card in chulsu:
        if next_card[card] != -1:
            n = next_card[card]
            ans.append(n)
            next_card[card] = next_card[n]
        else:
            index = bisect.bisect_right(minsu, card)
            n = minsu[index]
            ans.append(n)
            if index > 0:
                next_card[minsu[index-1]] = next_card[n]
            minsu = minsu[:index] + minsu[index+1:]

    return '\n'.join(map(str, ans))
    


def main():
    n, m, k = read_list_int()
    cards_minsu = read_list_int()
    cards_chulsu = read_list_int()
    print(solution(n, m, k, cards_minsu, cards_chulsu))


if __name__ == '__main__':
    main()