# Title: 제곱ㄴㄴ수
# Link: https://www.acmicpc.net/problem/1016
import math
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def num_nn_square(minimum, maximum):
    numbers = [True for _ in range(maximum-minimum+1)]
    count = len(numbers)
    n = 2
    while n*n <= maximum:
        n_square = n*n
        i = minimum // n_square
        while n_square*i <= maximum:
            index = n_square*i-minimum
            if index >= 0:
                if numbers[index]:
                    count -= 1
                    numbers[index] = False
            i += 1
        n += 1
    return count


if __name__ == '__main__':
    minimum, maximum = read_list_int()
    print(num_nn_square(minimum, maximum))