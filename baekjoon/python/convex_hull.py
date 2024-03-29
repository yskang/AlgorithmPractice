# Title: Convex Hull

import sys
from collections import deque
# import matplotlib.pyplot as plt

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '[{}, {}]'.format(self.x, self.y)

    def draw(self, plt):
        plt.scatter(self.x, self.y, 10)



def ccw(a: Point, b: Point, c: Point):
    """Counter Clock Wise.
    input 2 points a, b, c.
    return 1 for counter clock wise, -1 for clock wise, 0 for on a line.
    move all points to a posiotion on zero.
    rotate b and c to b on x axis
    if y coordinate of c is over the 0 then counter clock wise.
    elif y coordinate of c is under the 0 then clock wise.
    else y coordinate of c equal to zero, then on the line.
    """
    return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)


def get_lowest_dot(dots: list):
    min_y = 999999999
    min_y_dot = None
    min_y_idx = -1
    for i, dot in enumerate(dots):
        if dot.y < min_y:
            min_y = dot.y
            min_y_dot = dot
            min_y_idx = i
        elif dot.y == min_y:
            if dot.x < min_y_dot.x:
                min_y_dot = dot
    return min_y_dot, dots[:min_y_idx]+dots[min_y_idx+1:]


def sort_dots(dots: list, min_dot: Point):
    if len(dots) <= 1:
        return dots
    else:
        h = len(dots) // 2
        a = sort_dots(list(dots)[:h], min_dot)
        b = sort_dots(list(dots)[h:], min_dot)
        temp = []
        ia, ib = 0, 0
        while ia < len(a) and ib < len(b):
            if ccw(min_dot, a[ia], b[ib]) > 0:
                temp.append(a[ia])
                ia += 1
            elif ccw(min_dot, a[ia], b[ib]) == 0:
                if a[ia].x < b[ib].x:
                    temp.append(a[ia])
                    ia += 1
                else:
                    temp.append(b[ib])
                    ib += 1
            else:
                temp.append(b[ib])
                ib += 1
        if ia == len(a):
            temp += b[ib:]
        else:
            temp += a[ia:]
        return temp

def print_dots(dots: list, title: str):
    print(title)
    for dot in dots:
        print('{} '.format(dot.__str__()), end=' ')    


def convex_hull(dots: list):
    if len(dots) == 2:
        return dots

    min_dot, dots = get_lowest_dot(dots)
    dots = deque([min_dot] + sort_dots(dots, min_dot) + [min_dot])

    stack = deque()
    stack.append(dots.popleft())
    stack.append(dots.popleft())

    while dots:
        second = stack.pop()
        first = stack.pop()
        third = dots.popleft()

        if ccw(first, second, third) > 0:
            stack.append(first)
            stack.append(second)
            stack.append(third)
        else:
            stack.append(first)
            if len(stack) == 1:
                stack.append(third)
            else:
                dots.appendleft(third)

    return list(stack)[:-1]


def solution(n: int, dots: list):
    # _, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

    # for i, dot in enumerate(dots):
        # dot.draw(ax1)
        # ax1.annotate(i, (dot.x, dot.y))

    # for i, dot in enumerate(convex_hull(dots)):
    #     dot.draw(ax2)
    #     ax2.annotate(i, (dot.x, dot.y))
    # plt.show()
    dots = convex_hull(dots)
    print_dots(dots, 'hull')
    


def main():
    n = read_single_int()
    dots = []
    for _ in range(n):
        x, y = read_list_int()
        dots.append(Point(x, y))
    print(solution(n, dots))


if __name__ == '__main__':
    main()