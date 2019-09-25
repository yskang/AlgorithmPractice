# Title: 화성 지도
# Link: https://www.acmicpc.net/problem/3392

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def update_range(tree: list, start: int, end: int, value: int, offset: int):
    for pos in range(start, end+1):
        node = pos+offset
        tree[node] += value
    
    for node in range((start+offset)//2, ((end+offset)//2)+1):
        left = 1 if tree[node*2] > 0 else 0
        right = 1 if tree[node*2+1] > 0 else 0
        tree[node] = left + right

    left, right = (start+offset)//4, (end+offset)//4

    while True:
        r = list(range(left, right+1))
        for node in r:
            tree[node] = tree[node*2] + tree[node*2+1]
        if left <= 1 and right <= 1:
            break
        left //= 2
        right //= 2


def solution(n: int, pictures: list, y_max: int):
    tree = [0 for _ in range((y_max+1)*4)]
    x = 1
    offset = 0
    while True:
        offset = pow(2, x)
        if y_max+1 <= offset:
            break
        x += 1
    bars = []
    for x1, y1, x2, y2 in pictures:
        bars.append((x1, y1+1, y2, 1))
        bars.append((x2, y1+1, y2, -1))
    bars = sorted(bars, key=lambda k: k[0])

    ans = 0
    prev_x = 0
    for xx, y1, y2, val in bars:
        ans += (xx - prev_x) * tree[1]
        update_range(tree, y1, y2, val, offset-1)
        prev_x = xx
    return ans


def main():
    n = read_single_int()
    pictures = []
    y_max = 0
    for _ in range(n):
        x1, y1, x2, y2 = read_list_int()
        pictures.append([x1, y1, x2, y2])
        y_max = max(y_max, y1, y2)
    print(solution(n, pictures, y_max))


if __name__ == '__main__':
    main()