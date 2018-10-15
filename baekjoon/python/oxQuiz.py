# OX Quiz
# https://www.acmicpc.net/problem/8958

numOfcase = int(input())

for case in range(numOfcase):
    board = input()
    score = 0
    point = 0
    prev = 'X'
    for c in board:
        if c == 'O':
            prev = 'O'
            point = point + 1
            score = score + point
        else:
            prev = 'X'
            point = 0
    print(score)
