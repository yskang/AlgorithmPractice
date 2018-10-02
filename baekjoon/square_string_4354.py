# Title: 문자열 제곱
# Link: https://www.acmicpc.net/problem/4354

import sys

sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline().strip()


def get_p(str_in: str):
    origin_len = len(str_in)
    last_len = origin_len

    num_part = 2
    while len(str_in) >= num_part:
        while len(str_in) % num_part != 0:
            num_part += 1
        part_len = len(str_in) // num_part

        if str_in[:part_len] * num_part == str_in:
            str_in = str_in[:part_len]
            last_len = part_len
            num_part = 2
            continue
        else:
            num_part += 1

    return origin_len//last_len


if __name__ == '__main__':
    while True:
        in_str = read_single_str()
        if in_str == '.':
            break
        else:
            print(get_p(in_str))
