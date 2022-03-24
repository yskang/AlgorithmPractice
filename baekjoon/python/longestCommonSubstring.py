#
# https://www.acmicpc.net/problem/9249
import sys
from itertools import zip_longest, islice

def getLPC(str, sa, len_a):
    max_len = 0
    max_start = 0
    prev = sa[0]
    prev_side = False
    curr_side = False
    for line in sa[1:]:
        if prev < len_a:
            prev_side = False
        else:
            prev_side = True
        if line < len_a:
            curr_side = False
        else:
            curr_side = True

        if prev_side is not curr_side:
            min_len = min(len(str) - prev, len(str) - line)
            for i in range(min_len):
                if str[prev+i] is not str[line+i]:
                    if i > max_len:
                        max_len = i
                        max_start = prev
                    break
                if i == min_len-1:
                    if i+1 > max_len:
                        max_len = i + 1
                        max_start = line
        prev = line
    return max_len, max_start

def to_int_keys_best(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]

def suffix_array_best(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    return line

def inverse_array(l):
    n = len(l)
    ans = [0] * n
    for i in range(n):
        ans[l[i]] = i
    return ans

str_a = sys.stdin.readline()
str_b = sys.stdin.readline()

str = str_a + "!" + str_b
n = len(str)

suffix_array = inverse_array(suffix_array_best(str))
max_len, max_start = getLPC(str, suffix_array, len(str_a))
print(max_len)
print(str[max_start:max_start+max_len])
