# Title: KMP는 왜 KMP일까?
# Link: https://www.acmicpc.net/problem/2902
import sys
import functools
print(functools.reduce(lambda a, b: a+b , map(lambda a: a[0], sys.stdin.readline().strip().split('-'))))