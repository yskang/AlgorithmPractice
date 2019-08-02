# Title: 세로읽기
# Link: https://www.acmicpc.net/problem/10798

import sys


sys.setrecursionlimit(10 ** 6)


read_list_str = lambda: list(sys.stdin.readline().strip())


def solution(letters: list, max_len: int):
    for row in letters:
        if len(row) < max_len:
            row += ['*']*(max_len-len(row))
    res = ''
    for x in range(max_len):
        for y in range(5):
            res += letters[y][x]
    return res.replace('*', '')


def main():
    letters = []
    max_len = 0
    for _ in range(5):
        row = read_list_str()
        letters.append(row)
        max_len = max(max_len, len(row))
    print(solution(letters, max_len))


if __name__ == '__main__':
    main()