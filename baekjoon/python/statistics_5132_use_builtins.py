import sys
from statistics import median


def get_lfn(n_map):
    maxs = []
    max_val = 0
    for k in n_map:
        if max_val < n_map[k]:
            max_val = n_map[k]
            maxs = [k]
        elif max_val == n_map[k]:
            maxs.append(k)
    if len(maxs) == 1:
        return maxs[0]
    else:
        return sorted(maxs)[1]


if __name__ == "__main__":
    ns = []
    N = int(input())
    n_map = {}
    for i in range(N):
        n = int(sys.stdin.readline())
        ns.append(n)
        if n in n_map:
            n_map[n] += 1
        else:
            n_map[n] = 1

    print(round(sum(ns)/N))
    print(int(median(ns)))
    print(get_lfn(n_map))
    print(max(ns)-min(ns))