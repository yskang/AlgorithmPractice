# https://www.acmicpc.net/problem/2920
import sys

def get_scale(i):
    input_scale = list(map(int, i.strip().split(" ")))

    before = input_scale[0]
    direction = before < input_scale[1]
    for current in input_scale[1:]:
        if (before < current) != direction:
            return "mixed"
        before = current

    if direction:
        return "ascending"
    return "descending"

print(get_scale(sys.stdin.readline()))