# Title: 2루수 이름이 뭐야
# Link: https://www.acmicpc.net/problem/17350

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()


def solution(names: list):
    for name in names:
        if name == 'anj':
            return '뭐야;'
    return '뭐야?'


def main():
    n = read_single_int()
    names = []
    for _ in range(n):
        names.append(read_single_str())
    print(solution(names))


if __name__ == '__main__':
    main()