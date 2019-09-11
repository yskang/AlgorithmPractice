# Title: 기프티콘이 흘러넘쳐
# Link: https://www.acmicpc.net/problem/17420

import sys
from math import ceil
from collections import deque
from types import SimpleNamespace

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, rests: list, uses: list):
    giftcons = []
    for i in range(n):
        giftcons.append(SimpleNamespace(rest= rests[i], use= uses[i]))

    count = 0
    for i in range(n):
        giftcons = deque(sorted(giftcons, key=lambda x: x.use))

        use_gift = giftcons.popleft()

        if use_gift.rest < use_gift.use:
            extend = ceil((use_gift.use - use_gift.rest)/30)
            count += extend
            use_gift.rest += extend*30
        
        giftcons = sorted(giftcons, key=lambda x: x.rest)

        for giftcon in giftcons:
            if giftcon.use != use_gift.use and giftcon.rest < use_gift.rest:
                extend = ceil((use_gift.rest - giftcon.rest)/30)
                count += extend
                giftcon.rest += extend*30
            elif giftcon.rest >= use_gift.rest:
                break
    
    return count

    

def main():
    n = read_single_int()
    a = read_list_int()
    b = read_list_int()
    print(solution(n, a, b))


if __name__ == '__main__':
    main()