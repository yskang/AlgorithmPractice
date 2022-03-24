# https://www.acmicpc.net/problem/10250


def room_number(height, width, number):
    x = int((number+height-1) // height)
    y = int((number+height-1) % height)+1
    return "{}{:02d}".format(y, x)


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        info = list(map(int, input().split(" ")))
        print(room_number(info[0], info[1], info[2]))
