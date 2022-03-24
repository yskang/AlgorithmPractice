# Title: Self Representing Seq
# Link: https://www.acmicpc.net/problem/10220

import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def number_of_A(N):
    seq = [0 for _ in range(N)]
    found = True
    count = 0
    while True:
        # print(seq)
        for n, s in enumerate(seq):
            if seq.count(n) != s:
                found = False
                break
        if found:
            count += 1
        else:
            found = True

        increase = False
        for i, e in enumerate(seq):
            if e < N:
                seq[i] += 1
                increase = True
                break
            else:
                for j in range(i+1):
                    seq[j] = 0
                continue
        if not increase:
            break

    return count


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N = read_single_int()
        print(number_of_A(N))