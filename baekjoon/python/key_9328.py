# Title: 열쇠
# Link: https://www.acmicpc.net/problem/9328

import sys
from collections import deque

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split(' ')))


def read_single_int():
    return int(sys.stdin.readline().strip())


def read_single_str() -> str:
    return sys.stdin.readline().strip()


def solution(h: int, w: int, building: list, keys: set) -> int:
    documetns = 0
    doors = set()
    # dfs from edge of building, if block is '.' or key, then go to next block
    # if block is door and have a key for the door, then go to next block
    # if block is door and don't have a key for the door, then save the door position for next visit
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        if building[r][c] == '#':
            continue
        if building[r][c] == '$':
            documetns += 1
        building[r][c] = '#'
        for dr, dc in offsets:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h+2 and 0 <= nc < w+2:
                next_block = building[nr][nc]
                if next_block == '#':  # visited
                    continue
                if next_block == '*':  # wall
                    continue
                elif next_block == '.':  # empty block, can go
                    q.append((nr, nc))
                elif next_block.islower():  # key, add to keys and go to next block
                    keys.add(next_block)
                    q.append((nr, nc))
                elif next_block.isupper():  # door, if have a key, then go to next block, else save the door position
                    if next_block.lower() in keys:
                        q.append((nr, nc))
                    else:
                        doors.add((nr, nc))
                elif next_block == '$':
                    q.append((nr, nc))

    # for row in building:
    #     print(''.join(row))

    # print(keys)
    # print(doors)

    # after visit all possible blocks, then visit all doors that saved before
    # if have a key for the door, then visit the door and go to next block
    # if don't have a key for the door, then save the door position for next visit
    done = False
    new_doors = set()
    while not done:
        done = True
        doors = doors.union(new_doors)
        new_doors = set()
        for door in doors:
            r, c = door
            if building[r][c].lower() in keys:
                q = deque()
                q.append((r, c))
                while q:
                    rr, cc = q.popleft()
                    if building[rr][cc] == '#':
                        continue
                    if building[rr][cc] == '$':
                        documetns += 1
                    building[rr][cc] = '#'

                    for dr, dc in offsets:
                        nr, nc = rr + dr, cc + dc
                        if 0 <= nr < h+2 and 0 <= nc < w+2:
                            next_block = building[nr][nc]
                            if next_block == '#':
                                continue
                            if next_block == '.':
                                q.append((nr, nc))
                            elif next_block.islower():  # new key found
                                keys.add(next_block)
                                q.append((nr, nc))
                                done = False
                            elif next_block.isupper():
                                if next_block.lower() in keys:
                                    q.append((nr, nc))
                                else:
                                    new_doors.add((nr, nc))
                            elif next_block == '$':
                                q.append((nr, nc))
    return documetns


def main():
    t = read_single_int()
    for _ in range(t):
        h, w = read_list_int()
        building = []
        building.append(['.'] * (w+2))
        for _ in range(h):
            building.append(['.'] + list(read_single_str()) + ['.'])
        building.append(['.'] * (w+2))
        keys = set(read_single_str())
        print(solution(h, w, building, keys))


if __name__ == '__main__':
    main()