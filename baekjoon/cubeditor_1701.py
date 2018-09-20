# Title: Cubeditor
# Link: https://www.acmicpc.net/problem/1701

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def longest_substring(text: str):
    return text


if __name__ == '__main__':
    text = sys.stdin.readline()
    print(longest_substring(text))