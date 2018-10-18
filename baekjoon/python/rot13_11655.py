# Title: ROT13
# Link: https://www.acmicpc.net/problem/11655

import sys
import string

sys.setrecursionlimit(10 ** 6)

read_single_str = lambda: sys.stdin.readline()

def solution(s: str):
    ans = ''
    uppers = string.ascii_uppercase * 2
    lowers = string.ascii_lowercase * 2
    for c in s:
        if c.isupper():
            ans += uppers[ord(c)-ord('A')+13]
        elif c.islower():
            ans += lowers[ord(c)-ord('a')+13]
        else:
            ans += c
    return ans

def main():
    s = read_single_str()
    print(solution(s))


if __name__ == '__main__':
    main()