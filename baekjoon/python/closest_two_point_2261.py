#!/usr/bin/env python3

"""Get the minimum distance ** 2 among the given points.
>>> main("testcases/test_100000_1")
0
>>> main("testcases/test_10000_1")
144
>>> main("testcases/test_1000_1")
200
>>> main("testcases/test_uniform")
3969
"""

import math
import fileinput
from collections import defaultdict, deque


def load_points(input_file=None):
    """Read points from stdin and parse them to a list.

    input_file:
        The input file as a file object.
        Example usage:
            load_points('example.txt')
            load_points()  # Reads from stdin
    """
    # Not using with statement for python2 compatibility
    infile = fileinput.input(input_file)
    n_points = int(infile.readline())
    points = [int(x)+int(y)*1j for x, y in map(str.split, infile)]
    infile.close()
    assert len(points) == n_points
    return points


def mindist(points):
    """Get the minimum distance for the given points.

    points:
        list of points as a complex int.
        they should be sorted by x coordinate.
    """
    # 1. Getting the dimensions and upper bound
    xmin, xmax = points[0].real, points[-1].real
    ymin, ymax = points[0].imag, points[0].imag
    for p in points:
        if p.imag < ymin:
            ymin = p.imag
        elif p.imag > ymax:
            ymax = p.imag
    # We equally divide the bounding rectangle into k*k parts, where k*k<n.
    # According to the pigeonhole principle, there exists two points inside
    # one rectangle. The distance between those two points is no more than
    # math.hypot(width, height) / k.
    upper_bound = (math.hypot(xmax-xmin, ymax-ymin) /
                   math.floor(math.sqrt(len(points)-1)))

    # Workaround when minimum distance is zero or one.
    min_ = min(abs(points[i+1]-points[i]) for i in range(len(points)-1))
    if min_ in [0, 1]:
        return min_
    upper_bound = min(upper_bound, min_)

    # 2. Getting the minimum distance.
    # The minimum distance so far:
    min_ = upper_bound
    upper_bound_int = math.ceil(upper_bound)
    start = 0
    # Grouping of the points (in the queue) with similar y coordinates.
    group = [int(p.imag * 2 // upper_bound_int) for p in points]
    i_by_group = defaultdict(deque)
    # Pass the points through a queue.
    # The queue (points[start:stop]) can be represented as
    # merely two indices (start and stop).
    # Every iteration adds the last p into the queue.
    for stop, p in enumerate(points):
        # Points too left are popped out of the queue.
        while points[start].real <= p.real - min_:
            i = i_by_group[group[start]].popleft()
            assert start == i, (start, i)
            start += 1
        # Update minimum distance for the points inside the queue:
        # If two points have a difference > upper_bound_int,
        # Their group index has a difference of > 2.
        for check_group in range(group[stop]-2, group[stop]+3):
            for i in i_by_group[check_group]:
                min_ = min(min_, abs(p-points[i]))
        # Assign current point to group
        i_by_group[group[stop]].append(stop)
    return min_


def main(input_file=None):
    ps = load_points(input_file)
    ps.sort(key=lambda p: p.real)
    print(round(mindist(ps) ** 2))


if __name__ == '__main__':
    main()
