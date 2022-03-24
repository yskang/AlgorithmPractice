# Title: Count Circle Groups
# Link: https://www.acmicpc.net/problem/10216
import math
import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Node:
    def __init__(self, name, x, y, r):
        self.name = name
        self.child = set()
        self.x = x
        self.y = y
        self.r = r

    def add_child(self, node):
        self.child.add(node)


def dist_square(a, b):
    return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)


def dist_r_square(a, b):
    return (a.r + b.r) * (a.r + b.r)


def find_neighbors(enemies, target):
    for enemy in enemies:
        if enemy.name != target.name and dist_square(enemy, target) <= dist_r_square(enemy, target):
            target.child.add(enemy)


def dfs(enemies_, name, visited):
    if visited[name]:
        return
    visited[name] = True
    if len(enemies_[name].child) != 0:
        for enemy in enemies_[name].child:
            dfs(enemies_, enemy.name, visited)


def get_next(visited, enemies_):
    for enemy in enemies_:
        if not visited[enemy.name]:
            return enemy.name
    return None


def ccg(enemies, N):
    for enemy in enemies:
        find_neighbors(enemies, enemy)

    visited = collections.defaultdict(lambda: False)
    name = 0
    count = 1
    while True:
        dfs(enemies, name, visited)
        if len(visited) == N:
            return count
        name = get_next(visited, enemies)
        count += 1
        if name == Node:
            return


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N = read_single_int()
        enemies_input = []
        for i in range(N):
            x, y, r = read_list_int()
            enemies_input.append(Node(i, x, y, r))
        print(ccg(enemies_input, N))