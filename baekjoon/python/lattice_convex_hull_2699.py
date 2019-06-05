# Title: 격자점 컨벡스헐
# Link: https://www.acmicpc.net/problem/2699

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '{} {}'.format(self.x, self.y)

    def draw(self, plt):
        plt.scatter(self.x, self.y, 10)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


class ConvelHull:
    def __init__(self, dots: list):
        self.dots = dots
        self.lowest_dot = None
        self.highest_dot = None

    def ccw(self, a: Point, b: Point, c: Point):
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

    def get_low_and_high_dot(self):
        min_y = 999999999
        max_y = -99999999999
        min_y_dot = None
        max_y_dot = None
        min_y_idx = -1
        for i, dot in enumerate(self.dots):
            if dot.y < min_y:
                min_y = dot.y
                min_y_dot = dot
                min_y_idx = i
            elif dot.y == min_y:
                if dot.x < min_y_dot.x:
                    min_y_dot = dot
                    min_y_idx = i
            if dot.y > max_y:
                max_y = dot.y
                max_y_dot = dot
            elif dot.y == max_y:
                if dot.x < max_y_dot.x:
                    max_y_dot = dot
        self.lowest_dot = min_y_dot
        self.highest_dot = max_y_dot
        self.dots = self.dots[:min_y_idx]+self.dots[min_y_idx+1:]

    def sort_dots(self, dots: list):
        if len(dots) <= 1:
            return dots
        else:
            h = len(dots) // 2
            a = self.sort_dots(list(dots)[:h])
            b = self.sort_dots(list(dots)[h:])
            temp = []
            ia, ib = 0, 0
            while ia < len(a) and ib < len(b):
                if self.ccw(self.lowest_dot, a[ia], b[ib]) > 0:
                    temp.append(a[ia])
                    ia += 1
                elif self.ccw(self.lowest_dot, a[ia], b[ib]) == 0:
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

    def print_dots(self, title: str):
        print(title)
        for dot in self.dots:
            print('{} '.format(dot.__str__()), end=' ')    

    def get_hull(self):
        if len(self.dots) == 2:
            return self.dots

        self.get_low_and_high_dot()
        self.dots = deque([self.lowest_dot] + self.sort_dots(self.dots) + [self.lowest_dot])

        stack = deque()
        stack.append(self.dots.popleft())
        stack.append(self.dots.popleft())

        while self.dots:
            second = stack.pop()
            first = stack.pop()
            third = self.dots.popleft()

            if self.ccw(first, second, third) > 0:
                stack.append(first)
                stack.append(second)
                stack.append(third)
            else:
                stack.append(first)
                if len(stack) == 1:
                    stack.append(third)
                else:
                    self.dots.appendleft(third)

        if len(stack) == 2:
            return [stack[0], self.highest_dot]

        return list(stack)[:-1]


def solution(dots: list):
    points = []
    for i in range(0, len(dots), 2):
        points.append(Point(dots[i], dots[i+1]))

    convex_hull = ConvelHull(points)
    ans = []
    hull = convex_hull.get_hull()
    ans.append(len(hull))

    hull = deque(hull)
    while hull[-1] != convex_hull.highest_dot:
        hull.rotate()
    ans += reversed(hull)
    return '\n'.join(map(str, ans))


def main():
    p = read_single_int()
    for _ in range(p):
        n = read_single_int()
        dots = []
        for _ in range(((n-1)//5)+1):
            dots += read_list_int()
        print(solution(dots))


if __name__ == '__main__':
    main()