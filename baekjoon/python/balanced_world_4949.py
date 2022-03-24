# Title: 균형잡힌 세상
# Link: https://www.acmicpc.net/problem/4949

import sys
import string

sys.setrecursionlimit(10 ** 6)


def solution(line: str):
    parentheses = ['(', ')', '[', ']']
    new_line = ''
    for s in line:
        if s in parentheses:
            new_line += s

    while True:
        bbefore = len(new_line)
        while True:
            before = len(new_line)
            new_line = new_line.replace('()', '')
            if before == len(new_line):
                break
        
        while True:
            before = len(new_line)
            new_line = new_line.replace('[]', '')
            if before == len(new_line):
                break
        if bbefore == len(new_line):
            break
    
    return 'yes' if new_line == '' else 'no'


def main():
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '.':
            break
        print(solution(line))


if __name__ == '__main__':
    main()