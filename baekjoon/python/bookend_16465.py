# Title: Bookend
# Link: https://www.acmicpc.net/problem/16465

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(num_book: int, width_shelf: int, width_bookend: int, books: list):
    total_book_width = sum(books)
    if total_book_width > width_shelf:
        return -1
    if total_book_width == width_shelf:
        return 0
    if total_book_width < width_shelf and width_bookend <= total_book_width:
        return 1
    if total_book_width < width_shelf and (width_shelf-total_book_width) >= width_bookend:
        return 1
    return -1


def main():
    n, m, l = read_list_int()
    books = read_list_int()
    print(solution(n, m, l, books))


if __name__ == '__main__':
    main()