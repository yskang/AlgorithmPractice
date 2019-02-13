# Title: 3의 배수
# Link: https://www.acmicpc.net/problem/16561

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    case = 0

    for a in range(1, n):
        for b in range(a+1, n):
            if a % 3 == 0 and (b-a)%3 ==0 and (n-b)%3==0:
                case += 1

    return case


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()