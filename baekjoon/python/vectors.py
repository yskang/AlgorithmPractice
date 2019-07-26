import random
from types import SimpleNamespace
from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Vector2:
    def __init__(self, origin=None, target=None):
        self.x = target.x
        self.y = target.y
        if origin:
            self.x -= origin.x
            self.y -= origin.y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def reverse(self):
        self.x = -self.x
        self.y = -self.y
    
    def cross_direction(self, other):
        return self.x*other.y - self.y * other.x

def get_dist_square(a: Point, b: Point):
    return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)


def main():
    points = []
    coords = [(0, 6), (4, 5), (6, 4), (5, -6), (-4, -6), (-6, -5), (-6, 3), (-4, 5)]

    for x, y in coords:
        points.append(Point(x, y))

    left_points = deque(points)
    right_points = deque(points)
    
    left, right = Point(99999999999, 0), Point(-9999999999999, 0)
    l_index, r_index = -1, -1
    
    for i, point in enumerate(points):
        if point.x < left.x:
            left = point
            l_index = i
        if point.x > right.x:
            right = point
            r_index = i
    
    # print('left: {}. right: {}'.format(left, right))
    left_points.rotate(-l_index)
    right_points.rotate(-r_index)

    m_dist = 0
    m_points = [None, None]

    for _ in range(len(points)):
        dist = get_dist_square(left_points[0], right_points[0])
        if dist > m_dist:
            m_dist = dist
            m_points = [left_points[0], right_points[0]]

        v1 = Vector2(origin=left_points[0], target=left_points[1])
        v2 = Vector2(origin=right_points[0], target=right_points[1])
        v2.reverse()
        if v1.cross_direction(v2) > 0:
            right_points.rotate(-1)
        else:
            left_points.rotate(-1)

    print('max distance square: {}'.format(m_dist))
    print('({}) - ({})'.format(m_points[0], m_points[1]))


    


if __name__ == "__main__":
    main()