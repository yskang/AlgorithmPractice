# Title: 정사각형 진열
# Link: https://www.acmicpc.net/problem/1169

import sys


def read_single_int() -> int:
    return int(sys.stdin.readline().strip())


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, squares: list) -> str:
    squares = list(map(lambda x: x*2, squares))

    # deploy
    positions = []
    for i, square in enumerate(squares):
        max_x = squares[0]//2
        for j, front_square in enumerate(squares[:i]):
            if front_square == square:
                x = positions[j] + square
                if x > max_x:
                    max_x = x
            elif front_square < square:
                x = positions[j] + front_square
                if x > max_x:
                    max_x = x
            elif front_square > square:
                x = positions[j] + square
                if x > max_x:
                    max_x = x
        positions.append(max_x)
    # print(positions)

    ans = []
    # find square from top
    for i, square in enumerate(squares):
        left = positions[i] - square//2
        right = positions[i] + square//2
        ans.append(i+1)
        areas = []
        for j, other_square in enumerate(squares):
            other_left = positions[j] - other_square//2
            other_right = positions[j] + other_square//2
            if square < other_square:
                areas.append((other_left, other_right))

        # merge areas
        areas.sort(key=lambda x: x[0])
        merged_areas = []
        for area_left, area_right in areas:
            if not merged_areas:
                merged_areas.append((area_left, area_right))
            else:
                front_left, front_right = merged_areas[-1]
                if area_left <= front_right:
                    merged_areas.pop()
                    merged_areas.append((front_left, max(area_right, front_right)))
                else:
                    merged_areas.append((area_left, area_right))

        for area_left, area_right in merged_areas:
            if area_left <= left and right <= area_right:
                ans.pop()
                break

    return ' '.join(map(str, ans))


def main():
    n = read_single_int()
    squares = read_list_int()
    print(solution(n, squares))


if __name__ == '__main__':
    main()