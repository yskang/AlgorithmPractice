# Title: 색종이 만들기
# Link: https://www.acmicpc.net/problem/2630

import sys
from operator import add


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def cut(paper: list, x: int, y: int, width: int):
    if width == 1:
        if paper[y][x] == 1:
            return 0, 1
        return 1, 0
    
    half = width//2

    s = 0
    for row in paper[y:y+width]:
        s += sum(row[x:x+width])

    if s == 0:
        return 1, 0
    elif s == width*width:
        return 0, 1

    offsets = [[0, 0], [0, half], [half, 0], [half, half]]

    res = [0, 0]
    for offset_x, offset_y in offsets:
        res = map(add, res, cut(paper, x+offset_x, y+offset_y, half))
    return res


def solution(n: int, paper: list):
    return '\n'.join(map(str, cut(paper, 0, 0, n)))


def main():
    n = read_single_int()
    paper = []
    for _ in range(n):
        paper.append(read_list_int())
    print(solution(n, paper))


if __name__ == '__main__':
    main()