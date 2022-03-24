# Title: 지폐가 넘쳐흘러
# Link: https://www.acmicpc.net/problem/17422

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def get_max(n: int, ns: list, root: int, cache: list):
    if root > n:
        return 0
    if cache[root] != -1:
        return cache[root]
    res = ns[root] + max(get_max(n, ns, root*2, cache), get_max(n, ns, root*2+1, cache))
    cache[root] = res
    return res


def get(n: int, ns: list, q: int, cache: list, cache2: list):
    if cache2[q] != -1:
        return cache2[q]
    ans = ns[q] + get_max(n, ns, q*2, cache) + get_max(n, ns, q*2+1, cache)
    cache2[q] = ans
    return ans


def set_max_tree(tree: list, p: int, n: int):
    if p*2 > n:
        return
    tree[p] = max(tree[p*2], tree[p*2+1], tree[p])


def update_seg_max(tree: list, p: int, v: int, n: int):
    tree[p] = v
    k = p
    while True:
        set_max_tree(tree, k, n)
        k //= 2
        if k < 1:
            break


def init_seg_max(tree: list, values: list, p: int, n: int):
    if p > n:
        return -1
    left = init_seg_max(tree, values, p*2, n)
    right = init_seg_max(tree, values, p*2+1, n)

    if left == right == -1:
        tree[p] = values[p]
    else:
        tree[p] = max(left, right, values[p])
    return tree[p]


def solution(n: int, ns: list, q: int, qs: list):
    max_val = -1
    tree_1 = [-1 for _ in range(n+1)]
    tree_2 = [-1 for _ in range(n+1)]
    tree_3 = [-1 for _ in range(n+1)]

    for i in range(1, n+1):
        max_val = max(max_val, get(n, ns, i, tree_1, tree_2))

    init_seg_max(tree_3, tree_2, 1, n)

    print(tree_3[1])

    for num, val in qs:
        ns[num] = val

        k = num
        while True:
            tree_1[k] = -1
            get_max(n, ns, k, tree_1)
            if k == 1:
                break
            k //= 2

        k = num
        while True:
            tree_2[k] = -1
            v = get(n, ns, k, tree_1, tree_2)
            update_seg_max(tree_3, k, v, n)
            if k == 1:
                break
            k //= 2
        print(tree_3[1])


def main():
    n = read_single_int()
    ns = [0] + read_list_int()
    q = read_single_int()
    qs = []
    for _ in range(q):
        qs.append(read_list_int())
    solution(n, ns, q, qs)


if __name__ == '__main__':
    main()