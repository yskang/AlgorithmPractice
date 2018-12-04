# Title: close to 753
# Link: https://abc114.contest.atcoder.jp/tasks/abc114_b

import sys


sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def solution(s):
    return min(map(lambda x: abs(x-753), map(int, [s[i:i+3] for i in range(len(s)-2)])))


def main():
    s = read_single_str()
    print(solution(s))


if __name__ == '__main__':
    main()