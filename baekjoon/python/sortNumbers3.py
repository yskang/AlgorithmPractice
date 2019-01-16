# Title: 수 정렬하기 3
# Link: https://www.acmicpc.net/problem/10989

import sys


read_single_int = lambda: int(sys.stdin.readline().strip())


def main():
    sorted_ns = [0 for _ in range(10001)]
    n = read_single_int()
    for _ in range(n):
        sorted_ns[read_single_int()] += 1

    for i, n in enumerate(sorted_ns):
        if n > 0:
            print((str(i) + '\n') * n, end='')


if __name__ == '__main__':
    main()