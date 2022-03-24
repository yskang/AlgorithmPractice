# https://www.acmicpc.net/problem/11720
import sys
from functools import reduce

N = int(sys.stdin.readline())
print(reduce(lambda i, j: i + j, map(int, sys.stdin.readline().replace("\n", ""))))