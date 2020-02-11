# Title: 파괴된 도시
# Link: https://www.acmicpc.net/problem/18231

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_single_int = lambda: int(sys.stdin.readline().strip())


def solution(n: int, m: int, childs: list, k: int, destroyed: set):
    res = []
    need_to_destroy = set()
    for city in destroyed:
        for child in childs[city]:
            if child not in destroyed:
                need_to_destroy.add(city)
                break
        else:
            res.append(city)

    for city in res:
        for child in childs[city]:
            need_to_destroy.discard(child)

    if len(res) == 0:
        return -1

    if len(need_to_destroy) > 0:
        return -1 
        
    return f'{len(res)}\n{" ".join(map(str, res))}'


def main():
    n, m = read_list_int()
    cities = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = read_list_int()
        cities[u].append(v)
        cities[v].append(u)
    k = read_single_int()
    destoryed = set(read_list_int())
    print(solution(n, m, cities, k, destoryed))


if __name__ == '__main__':
    main()