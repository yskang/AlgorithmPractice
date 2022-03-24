# Title: Cupid
# Link: https://www.acmicpc.net/problem/16460

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip().split())
read_single_int = lambda: int(sys.stdin.readline().strip())

def solution(gender_prefer: str, geo_limit: int, profile: defaultdict):
    results = []
    for name in profile.keys():
        if profile[name][0] in gender_prefer and int(profile[name][1]) <= geo_limit:
            results.append(name)
    if not results:
        return 'No one yet'
    return '\n'.join(sorted(results))


def main():
    user, gender_prefer, geo_limit = read_list_str()
    n = read_single_int()
    profile = defaultdict(lambda: None)
    for _ in range(n):
        name, gender, distance = read_list_str()
        profile[name] = (gender, distance)

    print(solution(gender_prefer, int(geo_limit), profile))


if __name__ == '__main__':
    main()