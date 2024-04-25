# Title: 블록 쌓기
# Link: https://www.acmicpc.net/problem/14278

import sys
from collections import deque


MOD = 1000000007


def read_list_int() -> list:
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def get_possible_count(before: int, w: int, shapes: list, count: int) -> int:
    before = list(bin(before)[2:].zfill(w))
    blocks = [0, 1, 2, 3]
    for block in blocks:
        queue = deque()
        queue.append((block, w-1, 0))  # block, position, prev_shape
        while queue:
            block_size, position, prev_shape = queue.popleft()
            # check base
            if block_size == 0:
                if position < 0:
                    continue
                position -= 1
            elif block_size == 1:
                if position < 0:
                    continue
                if before[position] == '1':
                    prev_shape |= 1 << ((w-1)-position)
                    shapes[prev_shape] = (shapes[prev_shape] % MOD + count % MOD) % MOD
                else:
                    continue
                position -= 1
            elif block_size == 2:
                if position-1 < 0:
                    continue
                if before[position] == '1' and before[position-1] == '1':
                    prev_shape |= 3 << ((w-1)-position)
                    shapes[prev_shape] = (shapes[prev_shape] % MOD + count % MOD) % MOD
                else:
                    continue
                position -= 2
            elif block_size == 3:
                if position-2 < 0:
                    continue
                if before[position] == '1' and before[position-2] == '1':
                    prev_shape |= 7 << ((w-1)-position)
                    shapes[prev_shape] = (shapes[prev_shape] % MOD + count % MOD) % MOD
                else:
                    continue
                position -= 3
            else:
                continue
            for next_block in blocks:
                queue.append((next_block, position, prev_shape))


def solution(w: int, h: int) -> int:
    total = 1
    shapes = [0 for _ in range(2**w)]
    get_possible_count(2**w-1, w, shapes, 1)
    total += sum(shapes) % MOD
    for i in range(h-1):
        row = [0 for _ in range(2**w)]
        for shape, count in enumerate(shapes):
            if count > 0:
                get_possible_count(shape, w, row, count)
        shapes, row = row, shapes
        for s in shapes:
            total = (total % MOD + s % MOD) % MOD
    return total


def main():
    w, h = read_list_int()
    print(solution(w, h))


if __name__ == '__main__':
    main()