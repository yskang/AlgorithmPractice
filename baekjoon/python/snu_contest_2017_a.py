# Title: 여우 사인
# Link: https://www.acmicpc.net/problem/14709

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, pairs: list):
    if n < 3:
        return 'Woof-meow-tweet-squeek'
    
    a, b, c = False, False, False

    for pair in pairs:
        if 1 in pair and 3 in pair:
            a = True
            continue
        elif 4 in pair and 3 in pair:
            b = True
            continue
        elif 4 in pair and 1 in pair:
            c = True
            continue
        else:
            return 'Woof-meow-tweet-squeek'

    if a & b & c == True:
        return 'Wa-pa-pa-pa-pa-pa-pow!'
    else:
        return 'Woof-meow-tweet-squeek'


def main():
    n = read_single_int()
    pairs = []
    for _ in range(n):
        pairs.append(read_list_int())
    print(solution(n, pairs))


if __name__ == '__main__':
    main()