# Title: 숫자 카드 2
# Link: https://www.acmicpc.net/problem/10816

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, ns: list, m: int, ms: list):
    cards = defaultdict(lambda: 0)
    for number in ns:
        cards[number] += 1
    ans = []
    for number in ms:
        ans.append(str(cards[number]))
    return ' '.join(ans)
    

def main():
    n = read_single_int()
    ns = read_list_int()
    m = read_single_int()
    ms = read_list_int()
    print(solution(n, ns, m, ms))


if __name__ == '__main__':
    main()