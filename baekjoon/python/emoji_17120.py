# Title: 이모지
# Link: https://www.acmicpc.net/problem/17120

import sys
import re

sys.setrecursionlimit(10 ** 6)


read_line = lambda: sys.stdin.readline().strip()


def is_all_letter(content: str):
    if content == '':
        return False
    res = True
    for c in content:
        if 48 <= ord(c) <= 57:
            continue
        elif 65 <= ord(c) <= 90:
            continue
        elif 97 <= ord(c) <= 122:
            continue
        elif c == '+' or c == '-' or c == '_':
            continue
        else:
            return False
    return res


def solution(lines: list):
    for line in lines:

        # print(re.search("(?P<url>https?://[^\s]+)", line).group("url"))

        line = list(reversed(line))
        cat_found = False

        while line:
            c = line.pop()
            if c == ':':
                content = ''
                while line:
                    d = line.pop()
                    if d == ':':
                        if content == 'cat':
                            cat_found = True
                        break
                    content += d
                if len(line) > 0:
                    if not is_all_letter(content):
                        line.append(':')
                    if content == 'cat':
                        cat_found = True
                        break

        if cat_found:
            print('YES')
        else:
            print('NO')



def main():
    lines = []
    while True:
        line = read_line()
        if len(line) == 0:
            break
        lines.append(line)
    solution(lines)


if __name__ == '__main__':
    main()