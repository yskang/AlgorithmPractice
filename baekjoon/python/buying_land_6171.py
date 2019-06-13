# Title: 땅따먹기
# Link: https://www.acmicpc.net/problem/6171

import sys
from collections import deque
from bisect import bisect_left
import random

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

__min_cost = 99999999999999999999

def dp(i: int, lands: list, cache: list):
    if i < 0:
        return 0
    if cache[i] != -1:
        return cache[i]
    min_cost = 99999999999999999999
    for j in range(0, i+1):
        cost = dp(j-1, lands, cache) + lands[j][1] * lands[i][0]
        if cost < min_cost:
            min_cost = cost
    cache[i] = min_cost
    return min_cost


def solution_nn(n: int, lands: list):
    lands = deque(sorted(lands, key=lambda l: l[1]))
    lands = deque(sorted(lands, key=lambda l: l[0]))

    new_lands = deque()
    new_lands.append(lands.popleft())
    while lands:
        land = lands.popleft()
        while new_lands:
            last_height = new_lands[-1][1]
            if last_height > land[1]:
                new_lands.append(land)
                break
            else:
                new_lands.pop()
        if not new_lands:
            new_lands.append(land)

    cache = [-1 for _ in range(len(new_lands)+1)]
    min_cost = dp(len(new_lands)-1, new_lands, cache)
    return min_cost



def get_cross(poly_a: tuple, poly_b: tuple):
    return -1 * (poly_a[1] - poly_b[1]) / (poly_a[0] - poly_b[0])


def solution(n: int, lands: list):
    lands = deque(sorted(lands, key=lambda l: l[1]))
    lands = deque(sorted(lands, key=lambda l: l[0]))

    new_lands = deque()
    new_lands.append(lands.popleft())
    while lands:
        land = lands.popleft()
        while new_lands:
            last_height = new_lands[-1][1]
            if last_height > land[1]:
                new_lands.append(land)
                break
            else:
                new_lands.pop()
        if not new_lands:
            new_lands.append(land)

    cross_points = deque([0])
    polynomials = deque()
    width, height = new_lands[0]
    polynomials.append((height, 0))

    while len(new_lands) > 1:
        width, height = new_lands.popleft()
        i = bisect_left(cross_points, width)
        delta, y_cut = polynomials[i-1]
        min_value = delta*width + y_cut

        new_poly = (new_lands[0][1], min_value)
        top_poly = polynomials.pop()
        last_cross = cross_points.pop()
        cross = get_cross(top_poly, new_poly)

        if cross > last_cross:
            cross_points.append(last_cross)
            cross_points.append(cross)
            polynomials.append(top_poly)
            polynomials.append(new_poly)
        else:
            while polynomials:
                top_poly = polynomials.pop()
                last_cross = cross_points.pop()
                cross = get_cross(top_poly, new_poly)
                if cross > last_cross:
                    cross_points.append(last_cross)
                    cross_points.append(cross)
                    polynomials.append(top_poly)
                    polynomials.append(new_poly)
                    break

    delta, y_cut = polynomials[bisect_left(cross_points, new_lands[0][0])-1]
    
    return delta*new_lands[0][0]+y_cut


def main():
    n = read_single_int()
    lands = []
    for _ in range(n):
        lands.append(read_list_int())
    print(solution(n, lands))


def test():
    while True:
        n = random.randint(1, 10)
        lands = []
        for _ in range(n):
            lands.append((random.randint(1, 100), random.randint(1, 100)))
        try:
            a = solution(n, lands)
            b = solution_nn(n, lands)
            if a != b:
                print('diff! {} - {}'.format(a, b))
                print('{}'.format(n))
                for land in lands:
                    print('{} {}'.format(land[0], land[1]))
                break
            else:
                print('good')
        except:
            print('error!')
            print('{}'.format(n))
            for land in lands:
                print('{} {}'.format(land[0], land[1]))
            break
            

if __name__ == '__main__':
    # main()
    test()