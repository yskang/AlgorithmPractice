# Title: 민원이 넘쳐흘러
# Link: https://www.acmicpc.net/problem/17423

import sys
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class BIT:
    def __init__(self, n):
        self.n = n
        self.bit1 = defaultdict(lambda: 0)
        self.bit2 = defaultdict(lambda: 0)
    
    def _update(self, ft: list, p: int, v: int):
        while p <= self.n:
            ft[p] += v
            p += (p & (-p))

    def update_range(self, a: int, b: int, v: int):
        self._update(self.bit1, a, v)
        self._update(self.bit1, b+1, -v)
        self._update(self.bit2, a, v*(a-1))
        self._update(self.bit2, b+1, -v*b)

    def _query(self, ft: list, b: int):
        s = 0
        while b > 0:
            s += ft[b]
            b -= (b & (-b))
        return s

    def query(self, b: int):
        return self._query(self.bit1, b) * b - self._query(self.bit2, b)
    
    def query_range(self, a: int, b: int):
        return self.query(b) - self.query(a-1)


def check_collision(n: int, sizes: list, speakers: list, volume: int):
    ys_dic = defaultdict(lambda:-1)
    bars = []

    for x, y, size in speakers:
        bars.append((x-volume*size, y-volume*size, y+volume*size, 1))
        bars.append((x+volume*size, y-volume*size, y+volume*size, -1))
        ys_dic[y] = 1
        ys_dic[y-volume*size] = 1
        ys_dic[y+volume*size] = 1

    keys = sorted(ys_dic.keys())
    for i, v in enumerate(keys, 1):
        ys_dic[v] = i

    bars = sorted(bars, key=lambda x: (x[0], x[3]))

    bit = BIT(len(ys_dic)+1)
    bit_r = BIT(len(ys_dic)+1)
    for i in range(len(bars)):
        x, y_low, y_up, val = bars[i]
        if val == 1:
            if bit.query_range(ys_dic[y_low]+1, ys_dic[y_up]-1) != 0:
                return True
        bit.update_range(ys_dic[y_low], ys_dic[y_up], val)

        x, y_low, y_up, val = bars[len(bars)-i-1]
        if val == -1:
            if bit_r.query_range(ys_dic[y_low]+1, ys_dic[y_up]-1) != 0:
                return True
        bit_r.update_range(ys_dic[y_low], ys_dic[y_up], -val)
    return False


def solution(n: int, sizes: list, speakers: list):
    left = 1
    right = 1000001
    res = 0

    for i in range(n):
        speakers[i] = (speakers[i][0]-speakers[i][1], sum(speakers[i]), sizes[i])
    
    while left <= right:
        mid = (left + right) // 2

        if check_collision(n, sizes, speakers, mid):
            right = mid-1
        else:
            left = mid+1
            res = max(res, mid)
    return res


def main():
    n = read_single_int()
    sizes = read_list_int()
    speakers = []
    for _ in range(n):
        speakers.append(read_list_int())
    print(solution(n, sizes, speakers))


if __name__ == '__main__':
    main()