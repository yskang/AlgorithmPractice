# Title: 수 복원하기
# Link: https://www.acmicpc.net/problem/2312

import sys
from collections import defaultdict as ddict

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int):
    ans = ddict(lambda: 0)
    d = 2
    while n != 1:
        for i in range(d, n+1):
            if n % i == 0:
                a = n // i
                ans[i] += 1
                n = a
                break
    
    ret = []
    keys = ans.keys()
    for key in sorted(keys):
        ret.append('{} {}'.format(key, ans[key]))

    return '\n'.join(ret)


def main():
    t = read_single_int()
    for _ in range(t):
        n = read_single_int()
        print(solution(n))


if __name__ == '__main__':
    main()