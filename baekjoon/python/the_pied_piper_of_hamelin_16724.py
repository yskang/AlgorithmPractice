# Title: 피리부는 사나이
# Link: https://www.acmicpc.net/problem/16724

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()

offset = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

CONST = 10000

def find(x: int, parent: defaultdict):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x], parent)
        parent[x] = p
        return p

def union(x: int, y: int, parent: defaultdict):
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


def solution_union_find(rows: int, columns: int, world_map: list):
    # parent = defaultdict(lambda: None)
    parent = [i for i in range(rows * columns)]

    for y in range(rows):
        for x in range(columns):
            value = world_map[y][x]
            union(x+y*columns, x+offset[value][0] + (y+offset[value][1]) * columns, parent)

    # ps = set()
    # for key in parent:
    #     ps.add(find(key, parent))
    # return len(ps)
    count = 0
    for key in range(len(parent)):
        if key == parent[key]:
            count += 1
    return count


def solution_union_find_str(rows: int, columns: int, world_map: list):
    parent = defaultdict(lambda: None)
    for y in range(rows):
        for x in range(columns):
            k = '{},{}'.format(x,y)
            parent[k] = k

    for y in range(rows):
        for x in range(columns):
            value = world_map[y][x]
            union('{},{}'.format(x, y), '{},{}'.format(x+offset[value][0], (y+offset[value][1])), parent)

    # ps = set()
    # for key in parent:
    #     ps.add(find(key, parent))
    # return len(ps)

    count = 0
    for key in parent:
        if parent[key] == key:
            count += 1
    return count


def dfs(t: tuple, world_map: list, visited: defaultdict, count: int):
    if visited[t] != -1:
        if visited[t] == count:
            return 1
        return 0
    visited[t] = count
    arrow = world_map[t[1]][t[0]]
    return dfs((t[0] + offset[arrow][0], t[1] + offset[arrow][1]), world_map, visited, count)
    

def solution_dfs(rows: int, columns: int, world_map: list):
    visited = defaultdict(lambda: -1)
    count = 0
    t = 0
    for y in range(rows):
        for x in range(columns):
            if visited[(x, y)] == -1:
                count += dfs((x, y), world_map, visited, t)
                t += 1
    return count


def main():
    rows, columns = read_list_int()
    world_map = []
    for _ in range(rows):
        world_map.append(list(read_single_str()))
    print(solution_union_find(rows, columns, world_map))


if __name__ == '__main__':
    main()