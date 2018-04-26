import sys


def find_step_number(n):
    d = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(n-1):
        temp = [0]*10

        temp[1] = d[0]
        temp[8] = d[9]
        for i in range(1, 9):
            temp[i-1] += d[i]
            temp[i+1] += d[i]
        d = temp

    return sum(d)%1000000000


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(find_step_number(n))