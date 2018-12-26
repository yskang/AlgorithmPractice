# Title: 뚜루루 뚜루
# Link: https://www.acmicpc.net/problem/16129

import sys
import collections
import copy


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


class Cell:

    def __init__(self):
        self.value = ''
        self.total = 0
        self.edges = [0, 0, 0, 0] #bottom, top, right, left, in

    def __str__(self):
        return '[value: {}, total: {}, [{}, {}, {}, {}]]'.format(self.value, self.total, self.top, self.bottom, self.left, self.right)


def get_paths(m: list, x: int, y: int, w: int, h: int):
    duruduru = 'rrdr'
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]] # top, bottom, left, right
    translate = [1, 0, 3, 2]
    count = 0
    nexts = set()
    nexts.add((x, y))
    new_nexts = set()

    for nc in duruduru:
        for xx, yy in nexts:
            for d, direction in enumerate(directions):
                nx = xx+direction[0]
                ny = yy+direction[1]
                if 0 <= nx < w and 0 <= ny < h and m[ny][nx].value == nc:
                    v = m[yy][xx].total - m[yy][xx].edges[translate[d]]
                    if v > 0:
                        m[ny][nx].edges[d] = v
                        new_nexts.add((nx, ny))
                        m[yy][xx].edges[translate[d]] = -m[yy][xx].total

        print(new_nexts)

        for xx, yy in new_nexts:
            m[yy][xx].total = sum(m[yy][xx].edges)

        nexts, new_nexts = new_nexts, nexts
        new_nexts = set()

    for xx, yy in nexts:
        count += m[yy][xx].total
    
  
    print(count)
    print_map(m)
    return count


def print_map(m: list):
    for row in m:
        print(list(map(lambda x: x.total, row)))


def solution(r: int, c: int):
    m = [[Cell() for _ in range(c)] for _ in range(r)]
    s = collections.deque()

    s.append('d')
    s.append('r')
    s.append('r')
    s.append('d')
    s.append('r')

    for row in m:
        for i, _ in enumerate(row):
            row[i].value = s[0]
            s.rotate(-1)

    count = 0
    for y, row in enumerate(m):
        for x, cell in enumerate(row):
            if cell.value == 'd':
                temp = copy.deepcopy(m)
                temp[y][x].total = 1
                count += get_paths(temp, x, y, c, r)

    return count


def main():
    r, c = read_list_int()
    print(solution(r, c))


if __name__ == '__main__':
    main()