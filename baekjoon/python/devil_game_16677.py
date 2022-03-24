# Title: 악마 게임
# Link: https://www.acmicpc.net/problem/16677

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


def solution(m: str, n: int, words: list):
    no_jam_count = 0
    for j, [gap_word, _] in enumerate(words):
        is_no_jam = True
        idx = 0
        for i, c in enumerate(m):
            while idx < len(gap_word):
                if c == gap_word[idx]:
                    if i == len(m)-1:
                        is_no_jam = False
                    idx += 1
                    break
                else:
                    idx += 1
        if is_no_jam:
            words[j][1] = -1
            no_jam_count += 1
        else:
            words[j][1] = int(words[j][1]) / (len(gap_word) - len(m))

    if no_jam_count == len(words):
        return 'No Jam'

    max_score = 0
    max_word = ''
    for gw, sc in words:
        if sc != -1:
            if max_score < sc:
                max_score = sc
                max_word = gw
    return max_word


def main():
    m = read_single_str()
    n = read_single_int()
    words = []
    for _ in range(n):
        w, s = read_list_words()
        words.append([w, int(s)])
    print(solution(m, n, words))


if __name__ == '__main__':
    main()