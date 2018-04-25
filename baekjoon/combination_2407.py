import sys

if __name__ == '__main__':
    n, r = list(map(int, sys.stdin.readline().strip().split(' ')))
    com = [[0]*(n+1) for _ in range(r+1)]

    for r in range(1, r+1):
        for n in range(r, n+1):
            if r == 1:
                com[1][n] = n
            elif r == n:
                com[r][n] = 1
            else:
                com[r][n] = com[r-1][n-1] + com[r][n-1]
    print(com[r][n])