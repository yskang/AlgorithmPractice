# Title: Painting the Roof
# Link: https://www.acmicpc.net/problem/23428

import sys


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def solution(n: int, m: int, city_map: list) -> int:
    red, blue = 0, 0
    for row in city_map:
        red += row.count(1)
        blue += row.count(2)
    return max(red, blue) // 2


def main():
    n, m = read_list_int()
    city_map = []
    for _ in range(n):
        city_map.append(list(map(int, list(read_single_str()))))
    print(solution(n, m, city_map))


if __name__ == '__main__':
    main()