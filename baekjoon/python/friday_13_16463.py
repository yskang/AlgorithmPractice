# Title: 13일의 금요일
# Link: https://www.acmicpc.net/problem/16463

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())

normal_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoon_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_yoon(year: int):
    if year % 400 == 0:
        return True
    if year % 400 != 0 and year % 100 == 0:
        return False
    if year % 100 != 0 and year % 4 == 0:
        return True
    return False


def solution(end_year: int):
    count = 0
    day = 0
    for year in range(2019, end_year+1):
        for month in yoon_months if is_yoon(year) else normal_months:
            day = day + month
            if ((day - month) + 13 - 4) % 7 == 0:
                count += 1
    return count


def main():
    year = read_single_int()
    print(solution(year))


if __name__ == '__main__':
    main()