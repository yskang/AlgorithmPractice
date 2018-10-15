# https://www.acmicpc.net/problem/2908
from functools import reduce


def sangsoo_max(nums):
    return max(list(map(lambda a: int(reduce(lambda x, y: y+x, a)), nums)))


if __name__ == "__main__":
    nums = input().split(" ")
    print(sangsoo_max(nums))
