# https://www.acmicpc.net/problem/1157
import sys


def get_maximum_freq_alphabet(w):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {a: 0 for a in alpha}

    for c in w.upper():
        dic[c] += 1

    maxs = []
    max_num = -1

    for c in dic:
        if dic[c] > max_num:
            max_num = dic[c]
            maxs = [c]
        elif dic[c] == max_num:
            maxs.append(c)

    if len(maxs) == 1:
        return maxs[0]
    return "?"


if __name__ == "__main__":
    print(get_maximum_freq_alphabet(sys.stdin.readline().strip()))
