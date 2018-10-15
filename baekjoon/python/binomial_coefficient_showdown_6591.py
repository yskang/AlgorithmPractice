import sys

if __name__ == '__main__':
    n, r = -1, -1
    while n != 0 or r != 0:
        n, r = list(map(int, sys.stdin.readline().strip().split(' ')))
        if n == 0 and r == 0:
            break
        else:
            r = min(n-r, r)
            ans = 1

            for k in range(1, r+1):
                ans = ans * (n-k+1)//k

            print(ans)
