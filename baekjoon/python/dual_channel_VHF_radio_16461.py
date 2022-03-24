# Title: 듀얼 채널 VHF 무전기
# Link: https://www.acmicpc.net/problem/16461

import sys


sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_words = lambda: sys.stdin.readline().strip().split(' ')


def solution(a: int, b: int, current_ch: str, target_ch: int):
    count_a, count_b = 7, 7
    max_try_a = 7 if current_ch == 'A' else 6
    max_try_b = 7 if current_ch == 'B' else 6
    down_a, up_a, down_b, up_b = a, a, b, b

    for i in range(max_try_a):
        if target_ch == down_a or target_ch == up_a:
            count_a = i + (1 if current_ch == 'B' else 0)
            break
        down_a -= 20
        up_a += 20
        if down_a < 144000:
            down_a = 146000
        if up_a > 146000:
            up_a = 144000

    for i in range(max_try_b):
        if target_ch == down_b or target_ch == up_b:
            count_b = i + (1 if current_ch == 'A' else 0)
        down_b -= 20
        up_b += 20
        if down_b < 144000:
            down_b = 146000
        if up_b > 146000:
            up_b = 144000
    return min(count_a, count_b, 6)        



def main():
    t = read_single_int()
    for _ in range(t):
        a, b, current_ch, target_ch = read_list_words()
        print(solution(int(a.replace('.', '')), int(b.replace('.', '')), current_ch, int(target_ch.replace('.', ''))))


if __name__ == '__main__':
    main()