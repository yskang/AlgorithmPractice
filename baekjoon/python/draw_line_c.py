# Title: 선 그리기
# Link: https://www.acmicpc.net/problem/364/3

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, lines: list):
    projected = []
    for start, end in lines:
        projected.append((start, 's'))
        projected.append((end, 'e'))
    
    projected = sorted(projected, key=lambda x: x[0])

    length = 0
    start = 0
    open_count = 0
    for p, k in projected:
        if k == 's':
            if open_count == 0:
                start = p
            open_count += 1
        else:
            open_count -= 1
            if open_count == 0:
                length += (p - start)

    return length


def main():
    n = read_single_int()
    lines = []
    for _ in range(n):
        lines.append(read_list_int())
    print(solution(n, lines))


if __name__ == '__main__':
    main()