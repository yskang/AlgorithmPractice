# Title: 찾기
# Link: https://www.acmicpc.net/problem/1786

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_pi(pattern):
    ret = [0]

    for i in range(1, len(pattern)):
        j = ret[i-1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j-1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret


def find_pattern(text, pattern):
    pi = get_pi(pattern)
    result = []

    index_p = 0
    index_t = 0

    while index_t < len(text):
        if pattern[index_p] == text[index_t]:
            index_p += 1
            index_t += 1
            if index_p >= len(pattern):
                result += [index_t - len(pattern) + 1]
                index_p = 0 if index_p == 0 else pi[index_p - 1]
        else:
            index_t += 1 if index_p == 0 else 0
            index_p = 0 if index_p == 0 else pi[index_p - 1]

    return len(result), result


if __name__ == '__main__':
    T = sys.stdin.readline().replace('\n', '')
    P = sys.stdin.readline().replace('\n', '')
    count, positions = find_pattern(T, P)
    print(count)
    print(' '.join(map(str, positions)))
