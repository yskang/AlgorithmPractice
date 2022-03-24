# Title: 민원이 넘쳐흘러
# Link: https://www.acmicpc.net/problem/17423

import sys


sys.setrecursionlimit(10 ** 6)


read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


def solution(n: int, sizes: list, speakers: list):
    max_volume = 99999999999999
    x_sub_y_coord, x_plus_y_coord, x_coord, y_coord = [], [], [], []
    for i, (x, y) in enumerate(speakers):
        x_sub_y_coord.append((x-y, i, x+y))
        x_plus_y_coord.append((x+y, i, x-y))
        x_coord.append((x, i, y))
        y_coord.append((y, i, x))
    x_sub_y_coord = sorted(x_sub_y_coord, key=lambda z: (z[0], z[2]))
    x_plus_y_coord = sorted(x_plus_y_coord, key=lambda z: (z[0], z[2]))
    x_coord = sorted(x_coord, key=lambda z: (z[0], z[2]))
    y_coord = sorted(y_coord, key=lambda z: (z[0], z[2]))
    

    sames = []
    prev_pos, prev_i, _ = x_sub_y_coord[0]
    for current_pos, current_i, _ in x_sub_y_coord[1:]:
        if current_pos == prev_pos:
            sames.append(prev_i)
        elif sames:
            prev_i = sames[0]
            while sames:
                prev_i = sames.pop()
                t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
                t_max = max(0, t_max)
                max_volume = min(max_volume, t_max)
            sames = []
            continue

        t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
        t_max = max(0, t_max)
        max_volume = min(max_volume, t_max)
        prev_i = current_i
    
    _, prev_i, _ = x_plus_y_coord[0]
    for _, current_i, _ in x_plus_y_coord[1:]:
        if current_pos == prev_pos:
            sames.append(prev_i)
        elif sames:
            prev_i = sames[0]
            while sames:
                prev_i = sames.pop()
                t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
                t_max = max(0, t_max)
                max_volume = min(max_volume, t_max)
            sames = []
            continue

        t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
        t_max = max(0, t_max)
        max_volume = min(max_volume, t_max)
        prev_i = current_i

    _, prev_i, _ = x_coord[0]
    for _, current_i, _ in x_coord[1:]:
        if current_pos == prev_pos:
            sames.append(prev_i)
        elif sames:
            prev_i = sames[0]
            while sames:
                prev_i = sames.pop()
                t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
                t_max = max(0, t_max)
                max_volume = min(max_volume, t_max)
            sames = []
            continue

        t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
        t_max = max(0, t_max)
        max_volume = min(max_volume, t_max)
        prev_i = current_i
    
    _, prev_i, _ = y_coord[0]
    for _, current_i, _ in y_coord[1:]:
        if current_pos == prev_pos:
            sames.append(prev_i)
        elif sames:
            prev_i = sames[0]
            while sames:
                prev_i = sames.pop()
                t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
                t_max = max(0, t_max)
                max_volume = min(max_volume, t_max)
            sames = []
            continue

        t_max = (abs(speakers[current_i][0] - speakers[prev_i][0])+abs(speakers[current_i][1] - speakers[prev_i][1])) // (sizes[prev_i] + sizes[current_i])
        t_max = max(0, t_max)
        max_volume = min(max_volume, t_max)
        prev_i = current_i

    
    return max_volume


def main():
    n = read_single_int()
    sizes = read_list_int()
    speakers = []
    for _ in range(n):
        speakers.append(read_list_int())
    print(solution(n, sizes, speakers))


if __name__ == '__main__':
    main()