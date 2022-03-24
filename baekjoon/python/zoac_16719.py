# Title: 문제제목
# Link: https://www.acmicpc.net/problem/16719

import sys
from collections import defaultdict
from collections import deque


sys.setrecursionlimit(10 ** 6)


read_single_str = lambda: sys.stdin.readline().strip()

def get_word(word: list, show_list: list, x: int):
    ans = ''
    for i in range(len(word)):
        if show_list[i]:
            ans += word[i]
        if i == x:
            ans += word[i]
    return ans


def solution_bf(word: list):
    show_idx = [False for _ in range(len(word))]
    for _ in range(len(word)):
        word_list = []
        for i in range(len(word)):
            if not show_idx[i]:
                word_list.append((get_word(word, show_idx, i), i))
        sorted_words = sorted(word_list, key= lambda x: x[0])
        show_idx[sorted_words[0][1]] = True
        print(sorted_words[0][0])


def print_word(word: list, show: list):
    ans = ''
    for i in range(len(word)):
        if show[i]:
            ans += word[i]
    print(ans)


def find_minimum_letter(word: list, left: int, right: int, show_index: list):
    if left == right:
        return

    ziped_word = zip(word[left:right], [i for i in range(len(word))])
    sorted_word = sorted(ziped_word, key=lambda x: x[0])

    index = sorted_word[0][1]
    show_index[index + left] = True
    print_word(word, show_index)

    find_minimum_letter(word, left+index+1, right, show_index)
    find_minimum_letter(word, left, left+index, show_index)


def solution_recursion(word: list):
    show_index = [False for _ in word]
    find_minimum_letter(word, 0, len(word), show_index)


def main():
    word = read_single_str()
    solution_recursion(list(word))


if __name__ == '__main__':
    main()