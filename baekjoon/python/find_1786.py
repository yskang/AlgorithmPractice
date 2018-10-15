# Title: 찾기
# Link: https://www.acmicpc.net/problem/1786

import sys
import time
import logging

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_pi_optimized(pattern):
    ret = [0]

    for i in range(1, len(pattern)):
        j = ret[i-1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j-1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret


def get_pi(pattern):
    pi = [0]
    last_index = 0

    for index in range(1, len(pattern)):
        if pattern[index] == pattern[last_index]:
            pi.append(pi[-1] + 1)
            last_index += 1
        else:
            found = False
            while last_index > 0:
                last_index -= 1
                if pattern[last_index] == pattern[index]:
                    offset = 0
                    match = True
                    while last_index-offset > 0:
                        offset += 1
                        if pattern[last_index-offset] != pattern[index-offset]:
                            match = False
                            break
                    if match:
                        found = True
                        pi.append(last_index+1)
                        last_index += 1
                        break
            if not found:
                pi.append(0)
                last_index = 0
    return pi


def find_pattern(text, pattern):
    pi = get_pi(pattern)
    finds = []
    index_p, index_t = 0, 0
    
    while index_t < len(text):
        if pattern[index_p] == text[index_t]:
            index_t += 1
            index_p += 1
            if index_p == len(pattern):
                finds.append(index_t - index_p + 1)
                index_p = 0 if index_p == 0 else pi[index_p - 1]

        else:
            index_t += 1 if index_p == 0 else 0
            index_p = 0 if index_p == 0 else pi[index_p - 1]
            
    return len(finds), finds


if __name__ == '__main__':
    start_time = time.time()
    T = sys.stdin.readline().replace('\n', '')
    P = sys.stdin.readline().replace('\n', '')
    count, positions = find_pattern(T, P)
    print(count)
    print(' '.join(map(str, positions)))
    logging.warning('\nExecution time: {} seconds.'.format(time.time() - start_time))