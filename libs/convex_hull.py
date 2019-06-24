# Title: 볼록 껍질

import sys
from collections import deque
from math import atan2

sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.angle = 0
        self.dist_sq = 0
    
    def __str__(self):
        return '{} {}'.format(self.x, self.y)

    def draw(self, plt):
        plt.scatter(self.x, self.y, 10)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y > other.y:
            return False
        else:
            if self.x < other.x:
                return True
            return False
    
    def set_angle(self, base):
        self.angle = atan2(self.y-base.y, self.x-base.x)

    def set_dist_sq(self, base):
        self.dist_sq = (self.y-base.y)**2 + (self.x-base.x)**2
    
    def get_dist_sq(self, other):
        return (self.x-other.x)**2 + (self.y-other.y)**2


class ConvelHull:
    def __init__(self, dots: list):
        self.dots = dots
        self.lowest_dot = None
        self.highest_dot = None
        self.convel_hull = None
        self.leftest_dot = None

    def ccw(self, a: Point, b: Point, c: Point):
        return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)

    def get_low_and_high_dot(self):
        self.lowest_dot = min(self.dots)
        self.highest_dot = max(self.dots)
        # left_x = min(self.dots, key=lambda d: d.x).x
        # left_x_dots = list(filter(lambda d: d.x==left_x, self.dots))
        # self.leftest_dot = min(left_x_dots, key=lambda d:d.y)

    def print_dots(self, title: str):
        print(title)
        for dot in self.dots:
            print('{} '.format(dot.__str__()), end=' ')
    
    def sort_dots(self):
        for dot in self.dots:
            dot.set_angle(self.lowest_dot)
            dot.set_dist_sq(self.lowest_dot)

        self.dots = sorted(self.dots, key= lambda d: d.dist_sq)
        self.dots = sorted(self.dots, key= lambda d: d.angle)

        last_same_angles = []
        prev_angle = self.dots[-1].angle
        for dot in reversed(self.dots):
            if dot.angle == prev_angle:
                last_same_angles.append(dot)
            else:
                break
        self.dots = self.dots[:-len(last_same_angles)] + last_same_angles


    def get_hull(self, only_edge=True):
        if len(self.dots) == 2:
            return self.dots

        self.get_low_and_high_dot()
        self.sort_dots()

        self.dots += [self.lowest_dot]
        self.dots = deque(self.dots)

        stack = deque()
        stack.append(self.dots.popleft())
        stack.append(self.dots.popleft())

        while self.dots:
            second = stack.pop()
            first = stack.pop()
            third = self.dots.popleft()

            is_ccw = self.ccw(first, second, third)

            if is_ccw > 0:
                stack.append(first)
                stack.append(second)
                stack.append(third)
            elif not only_edge and is_ccw == 0:
                stack.append(first)

                ds = first.get_dist_sq(second)
                dt = first.get_dist_sq(third)

                if ds <= dt:
                    stack.append(second)
                    stack.append(third)
                else:
                    stack.append(third)
                    stack.append(second)
            else:
                stack.append(first)
                if len(stack) == 1:
                    stack.append(third)
                else:
                    self.dots.appendleft(third)

        if len(stack) == 2:
            return [stack[0], self.highest_dot]

        stack.pop()
        self.convel_hull = list(stack)
        return stack

    def get_area(self):
        first, second = 0, 0
        self.convel_hull.append(self.convel_hull[0])
        prev_dot = self.convel_hull[0]
        for dot in self.convel_hull[1:]:
            first += (prev_dot.x * dot.y)
            second += (prev_dot.y * dot.x)
            prev_dot = dot
        return 0.5 * abs(first - second)

def solution(n: int, dots: list):
    hull = ConvelHull(dots)
    return len(hull.get_hull())


def main():
    n = read_single_int()
    dots = []
    for _ in range(n):
        x, y = read_list_int()
        dots.append(Point(x, y))
    print(solution(n, dots))


if __name__ == '__main__':
    main()