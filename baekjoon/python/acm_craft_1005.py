import sys

sys.setrecursionlimit(10**6)


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def get_min_time(n, reqs, delay, cache):
    if n in cache:
        return cache[n]

    if n not in reqs:
        cache[n] = delay[n-1]
        return delay[n-1]

    max_d = 0
    for x in reqs[n]:
        max_d = max(max_d, cache[x] if x in cache else get_min_time(x, reqs, delay, cache))

    cache[n] = max_d + delay[n-1]
    return max_d + delay[n-1]


if __name__ == '__main__':
    T = read_single_int()
    for _ in range(T):
        N, K = read_list_int()
        D = read_list_int()
        req_map = {}
        for i in range(K):
            f, t = read_list_int()
            if t not in req_map:
                req_map[t] = [f]
            else:
                req_map[t].append(f)
        W = read_single_int()
        cache = {}
        print(get_min_time(W, req_map, D, cache))
