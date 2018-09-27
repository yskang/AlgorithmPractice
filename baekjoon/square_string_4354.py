# Title: 문자열 제곱
# Link: https://www.acmicpc.net/problem/4354

import sys


sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip())



def find_pattern(text: str, pattern: str):
    finds = []
    index_p, index_t = 0, 0
    
    while index_t < len(text):
        if pattern[index_p] == text[index_t]:
            index_t += 1
            index_p += 1
            if index_p == len(pattern):
                finds.append(index_t - index_p + 1)
                index_p = 0

        else:
            return []
            
    return finds


def find_n(ins: str, ans: list, len_ins: int):
    length = len(ins)
    i = 2
    while length != 1:
        while i <= len(ins):
            if len(ins) % i == 0:
                length = len(ins)//i
                break
            else:
                i += 1
        finds = find_pattern(ins, ins[:length])
        if len(finds) * length == len(ins):
            ans.append(len_ins // length)
            find_n(ins[:length], ans, len_ins)
            return
        i += 1
    return


if __name__ == '__main__':
    while True:
        ins = read_list_str()
        if ins == ['.']:
            break
        else:
            ans = [1]
            find_n(ins, ans, len(ins))
            print(max(ans))
