# Title: Cubeditor
# Link: https://www.acmicpc.net/problem/1701

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_pi(pattern):
    pi = [0]
    last_index = 0

    for index in range(1, len(pattern)):
        if pattern[index] == pattern[last_index]:
            pi.append(pi[-1] + 1)
            last_index += 1
        else:
            found = False
            while last_index > 0:
                last_index -= 1
                if pattern[last_index] == pattern[index]:
                    offset = 0
                    match = True
                    while last_index-offset > 0:
                        offset += 1
                        if pattern[last_index-offset] != pattern[index-offset]:
                            match = False
                            break
                    if match:
                        found = True
                        pi.append(last_index+1)
                        last_index += 1
                        break
            if not found:
                pi.append(0)
                last_index = 0
    return pi


def longest_substring(text: str):
    start = 0
    max_len = 0
    for start in range(0, len(text)):
        pi = get_pi(text[start:])
        max_len = max(max_len, max(pi))
    return max_len


if __name__ == '__main__':
    text = sys.stdin.readline()
    print(longest_substring(text))