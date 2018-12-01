# Title: 탈출
# Link: https://www.acmicpc.net/problem/d

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def button_b(n: int):
    nn = str(int(str(2*n)[0]) - 1)
    nnn = str(2*n)[1:]
    ans = int(nn+nnn)
    return ans


def solution(n: int, t: int, g: int):
    num = n
    for i in range(t):
        bb_num = button_b(num)
        if bb_num == g:
            return i
        elif bb_num < g:
            num = bb_num
        else:
            num += 1
            if num == g:
                return i
    return 'ANG'
            


def main():
    n, t, g = read_list_int()
    print(solution(n, t, g))


if __name__ == '__main__':
    main()