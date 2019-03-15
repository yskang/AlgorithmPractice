# Title: 문제제목
# Link: https://www.acmicpc.net/problem/numpy

import sys
import numpy as np
from numpy.linalg import matrix_power

sys.setrecursionlimit(10 ** 6)



def solution():
    a = np.array([[1, 0, 0, 1],
                  [1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0]])
    b = np.array([[1],
                  [0],
                  [0],
                  [0]])

    r = matrix_power(a, 10000000)
    x = np.matmul(r, b)
    print(x[0][0])


def main():
    print(solution())


if __name__ == '__main__':
    main()