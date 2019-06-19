# Title: 땅따먹기
# Link: https://www.acmicpc.net/problem/6171

import sys
from collections import deque
from bisect import bisect_left
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

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


def solution(n: int, lands: list, ylim=550):
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

    xs = [i for i in range(-10, new_lands[-1][0]*2)]

    fig = plt.figure()
    plt.ion()
    plt.show()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim([-10, xs[-1]])
    ax.set_ylim([-10, ylim*2])
    ax.axhline(y=0, color='gray', linestyle='--')
    ax.axvline(x=0, color='gray', linestyle='--')
    plt.draw()
    plt.pause(0.01)
    input('enter to continue.')

    cross_points = deque([0])
    polynomials = deque()
    width, height = new_lands[0]
    polynomials.append((height, 0))

    ax.plot(xs, list(map(lambda x: polynomials[0][0]*x, xs)), color='tab:cyan')
    plt.draw()
    plt.pause(0.01)
    input('enter to continue.')

    while len(new_lands) > 1:
        width, height = new_lands.popleft()
        i = bisect_left(cross_points, width)
        delta, y_cut = polynomials[i-1]
        min_value = delta*width + y_cut

        ax.scatter([width], [0], color='tab:blue')
        ax.axvline(x=width, color='blue', linestyle='--')
        plt.draw()
        plt.pause(0.01)
        input('enter to continue.')

        ax.scatter([0], [min_value], color='tab:blue')
        ax.axhline(y=min_value, color='blue', linestyle='--')
        plt.draw()
        plt.pause(0.01)
        input('enter to continue.')

        new_poly = (new_lands[0][1], min_value)
        top_poly = polynomials.pop()
        last_cross = cross_points.pop()
        cross = get_cross(top_poly, new_poly)

        ax.plot(xs, list(map(lambda x: new_poly[0]*x+new_poly[1], xs)), color='yellow')
        plt.draw()
        plt.pause(0.01)
        input('enter to continue.')

        ax.plot(xs, list(map(lambda x: top_poly[0]*x+top_poly[1], xs)), color='tab:green')
        plt.draw()
        plt.pause(0.01)
        input('enter to continue.')

        ax.scatter([cross], [0], color='yellow')
        ax.axvline(x=cross, color='yellow', linestyle='--')
        plt.draw()
        plt.pause(0.01)
        input('enter to continue.')

        if cross > last_cross:
            cross_points.append(last_cross)
            cross_points.append(cross)
            polynomials.append(top_poly)
            polynomials.append(new_poly)

            ax.plot(xs, list(map(lambda x: top_poly[0]*x+top_poly[1], xs)), color='tab:cyan')
            plt.draw()
            plt.pause(0.01)
            input('enter to continue.')

            ax.plot(xs, list(map(lambda x: new_poly[0]*x+new_poly[1], xs)), color='tab:cyan')
            plt.draw()
            plt.pause(0.01)
            input('enter to continue.')

        else:
            while polynomials:
                ax.plot(xs, list(map(lambda x: top_poly[0]*x+top_poly[1], xs)), color='white')
                plt.draw()
                plt.pause(0.01)
                input('enter to continue.')

                top_poly = polynomials.pop()
                last_cross = cross_points.pop()
                cross = get_cross(top_poly, new_poly)
                
                ax.plot(xs, list(map(lambda x: top_poly[0]*x+top_poly[1], xs)), color='tab:green')
                plt.draw()
                plt.pause(0.01)
                input('enter to continue.')

                ax.scatter([cross], [0], color='yellow')
                ax.axvline(x=cross, color='yellow', linestyle='--')
                plt.draw()
                plt.pause(0.01)
                input('enter to continue.')

                if cross > last_cross:
                    cross_points.append(last_cross)
                    cross_points.append(cross)
                    polynomials.append(top_poly)
                    polynomials.append(new_poly)

                    ax.plot(xs, list(map(lambda x: top_poly[0]*x+top_poly[1], xs)), color='tab:cyan')
                    plt.draw()
                    plt.pause(0.01)
                    input('enter to continue.')

                    ax.plot(xs, list(map(lambda x: new_poly[0]*x+new_poly[1], xs)), color='tab:cyan')
                    plt.draw()
                    plt.pause(0.01)
                    input('enter to continue.')

                    break

    delta, y_cut = polynomials[bisect_left(cross_points, new_lands[0][0])-1]

    ax.scatter([new_lands[0][0]], [0], color='red')
    ax.axvline(x=new_lands[0][0], color='red', linestyle='-')
    plt.draw()
    plt.pause(0.01)
    input('enter to continue.')

    ax.plot(xs, list(map(lambda x: delta*x+y_cut, xs)), color='red')
    plt.draw()
    plt.pause(0.01)
    input('enter to continue.')

    ax.scatter([delta*new_lands[0][0]+y_cut], [0], color='red')
    ax.axhline(y=delta*new_lands[0][0]+y_cut, color='red', linestyle='-')
    plt.draw()
    plt.pause(0.01)
    input('enter to continue.')

    return delta*new_lands[0][0]+y_cut


def main():
    n = read_single_int()
    lands = []
    for _ in range(n):
        lands.append(read_list_int())
    print(solution(n, lands))


def test():
    while True:
        n = random.randint(1, 50)
        lands = []
        for _ in range(n):
            lands.append((random.randint(1, 100), random.randint(1, 100)))
        try:
            b = solution_nn(n, lands)
            a = solution(n, lands, b+50)
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