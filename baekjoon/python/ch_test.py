# Title: 볼록 껍질
# Link: https://www.acmicpc.net/problem/1708

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
            if self.x < other.y:
                return True
            return False
    
    def set_angle(self, base):
        self.angle = atan2(self.y-base.y, self.x-base.x)

    def set_dist_sq(self, base):
        self.dist_sq = (self.y-base.y)**2 + (self.x-base.x)**2


class ConvelHull:
    def __init__(self, dots: list):
        self.dots = dots
        self.lowest_dot = None
        self.highest_dot = None
        self.convel_hull = None
        self.on_the_lines = []

    def ccw(self, a: Point, b: Point, c: Point):
        return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)

    def get_low_and_high_dot(self):
        self.lowest_dot = min(self.dots)
        self.highest_dot = max(self.dots)

    def print_dots(self, title: str):
        print(title)
        for dot in self.dots:
            print('{} '.format(dot.__str__()), end=' ')    

    def get_hull(self):
        if len(self.dots) == 2:
            return self.dots

        self.get_low_and_high_dot()

        for dot in self.dots:
            dot.set_angle(self.lowest_dot)
            dot.set_dist_sq(self.lowest_dot)

        self.dots = sorted(self.dots, key= lambda d: d.dist_sq)
        self.dots = deque(sorted(self.dots, key= lambda d: d.angle))
        self.dots += [self.lowest_dot]

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
            elif is_ccw == 0:
                stack.append(first)
                if len(stack) == 1:
                    stack.append(third)
                    self.on_the_lines.append(second)
                else:
                    self.dots.appendleft(third)
                    self.on_the_lines.append(second)
            else:
                stack.append(first)
                if len(stack) == 1:
                    stack.append(third)
                else:
                    self.dots.appendleft(third)

        self.convel_hull = list(stack)[:-1]
        return list(stack)[:-1]

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