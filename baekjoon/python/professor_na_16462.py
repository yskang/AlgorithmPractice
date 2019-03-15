# Title: 나 교수님의 악필
# Link: https://www.acmicpc.net/problem/16461

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_single_str = lambda: sys.stdin.readline().strip()


def solution(n: int, scores: list):
    s = 0
    for score in scores:
        score = score.replace('0', '9').replace('6', '9')
        
        if int(score) > 100:
            s += 100
        else:
            s += int(score)
    v, r = divmod(s, n)
    if r == 0:
        return v
    elif s/n - v < 0.5:
        return v
    else:
        return v+1


def main():
    n = read_single_int()
    scores = []
    for _ in range(n):
        scores.append(read_single_str())
    print(solution(n, scores))


if __name__ == '__main__':
    main()