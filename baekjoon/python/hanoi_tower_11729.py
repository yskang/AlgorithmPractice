# Title: 하노이 탑 이동 순서
# Link: https://www.acmicpc.net/problem/11729

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())

def hanoi(n, from_p, to_p, aux, ans):
    if n == 1:
        ans.append('{} {}'.format(from_p, to_p))
        return
    hanoi(n-1, from_p, aux, to_p, ans)
    ans.append('{} {}'.format(from_p, to_p))
    hanoi(n-1, aux, to_p, from_p, ans)


def solution(n: int):
    ans = []
    hanoi(n, 1, 3, 2, ans)
    return str(len(ans)) + '\n' + '\n'.join(ans)


def main():
    n = read_single_int()
    print(solution(n))


if __name__ == '__main__':
    main()