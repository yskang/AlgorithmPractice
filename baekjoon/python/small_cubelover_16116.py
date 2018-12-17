# Title: 작은 큐브러버
# Link: https://www.acmicpc.net/problem/16116

import sys
import collections


sys.setrecursionlimit(10 ** 6)

read_list_str = lambda: list(sys.stdin.readline().strip().split())


def solution(colors: list):
    whilte_cubes = []
    opp_cubes = []

    for color in colors:
        if 'W' in color:
            i = color.index('W')
            if i == 0:
                whilte_cubes.append(color[1:3])
            elif i == 1:
                whilte_cubes.append([color[2], color[0]])
            else:
                whilte_cubes.append(color[0:2])

    
    color_string = 'BGORY'
    for cube in whilte_cubes:
        for color in cube:
            color_string = color_string.replace(color, '')
            if color_string == '':
                return 'NO'

    if len(color_string) != 1:
        return 'NO'
    
    opp_color = color_string

    for color in colors:
        if opp_color in color:
            i = color.index(opp_color)
            if i == 0:
                opp_cubes.append(color[1:3])
            elif i == 1:
                opp_cubes.append([color[2], color[0]])
            else:
                opp_cubes.append(color[0:2])

    
    new_white_cubes = [whilte_cubes[0]]
    whilte_cubes = whilte_cubes[1:]

    for _ in range(3):
        found = False
        for white_cube in whilte_cubes:
            if white_cube[0] == new_white_cubes[-1][1]:
                found = True
                new_white_cubes.append(white_cube)
                break
        if found:
            whilte_cubes.remove(white_cube)
    
    if len(new_white_cubes) != 4:
        return 'NO'
    
    for white_cube in new_white_cubes:
        if list(reversed(white_cube)) in opp_cubes:
            opp_cubes.remove(list(reversed(white_cube)))
    
    if opp_cubes == []:
        return 'YES'
    
    return 'NO'



def main():
    colors = []
    for _ in range(8):
        colors.append(read_list_str())
    print(solution(colors))


if __name__ == '__main__':
    main()