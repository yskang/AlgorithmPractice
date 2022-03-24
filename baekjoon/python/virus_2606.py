# Title: 바이러스
# Link: https://www.acmicpc.net/problem/2606
import itertools
import sys

import collections

sys.setrecursionlimit(10 ** 6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


class Node:
    def __init__(self, name):
        self.name = name
        self.child = set()

    def add_child(self, node):
        self.child.add(node)

    def __str__(self):
        return '[name: {}, child: {}]'.format(self.name, self.child)


def dfs(computers, name, visited):
    if visited[name]:
        return
    visited[name] = True
    for computer in computers[name].child:
        dfs(computers, computer.name, visited)


def get_number_of_infection(computers, num_computer):
    # for computer in computers.values():
    #     print(computer)
    visited = collections.defaultdict(lambda: False)
    dfs(computers, 1, visited)
    return len(visited)-1


if __name__ == '__main__':
    num_computer = read_single_int()
    connects = read_single_int()
    computers = collections.defaultdict(lambda: None)
    for _ in range(connects):
        a, b = read_list_int()
        if computers[a] is None:
            computers[a] = Node(a)
        if computers[b] is None:
            computers[b] = Node(b)
        computers[a].add_child(computers[b])
        computers[b].add_child(computers[a])
    print(get_number_of_infection(computers, num_computer))