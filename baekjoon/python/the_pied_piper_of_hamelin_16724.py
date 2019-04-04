# Title: 피리부는 사나이
# Link: https://www.acmicpc.net/problem/16724

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_str = lambda: sys.stdin.readline().strip()

offset = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

def find(x: tuple, parent: defaultdict):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x], parent)
        parent[x] = p
        return p

def union(x: tuple, y: tuple, parent: defaultdict):
    x = find(x, parent)
    y = find(y, parent)
    if x != y:
        parent[y] = x


def solution_union_find(rows: int, columns: int, world_map: list):
    parent = defaultdict(lambda: None)
    for y in range(rows):
        for x in range(columns):
            parent[(x, y)] = (x, y)

    for y in range(rows):
        for x in range(columns):
            value = world_map[y][x]
            union((x, y), (x+offset[value][0], y+offset[value][1]), parent)

    ps = []
    for key in parent:
        ps.append(find(key, parent))
    return len(set(ps))



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
    print(solution_dfs(rows, columns, world_map))


if __name__ == '__main__':
    main()