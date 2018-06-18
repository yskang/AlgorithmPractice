# Title: 제곱ㄴㄴ수
# Link: https://www.acmicpc.net/problem/1016
import math
import sys

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def is_nn(num):
    for n in range(2, int(math.sqrt(num))+1):
        if num % n**2 == 0:
            return True
    return False


def num_nn_square(minimum, maximum):
    numbers = [1 for _ in range(minimum, maximum+1)]
    n = 2
    while True:
        nn = n**2
        d = 1
        while True:
            nn *= d
            numbers[nn] = 0
            d += 1


    return sum(numbers)


if __name__ == '__main__':
    minimum, maximum = read_list_int()
    print(num_nn_square(minimum, maximum))