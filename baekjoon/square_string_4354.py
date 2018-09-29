# Title: 문자열 제곱
# Link: https://www.acmicpc.net/problem/4354

import sys

sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def find_n(ins: str, ans: list, len_ins: int):
    length = len(ins)
    i = 2
    while length != 1:
        while i <= len(ins):
            if len(ins) % i == 0:
                length = len(ins)//i
                break
            else:
                i += 1
        if ins[:length]*(len(ins)//length) == ins:
            ans.append(len_ins // length)
            find_n(ins[:length], ans, len_ins)
            return
        i += 1
    return


if __name__ == '__main__':
    while True:
        in_str = read_single_str()
        if in_str == '.':
            break
        else:
            ans = [1]
            find_n(in_str, ans, len(in_str))
            print(max(ans))
