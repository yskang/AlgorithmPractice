import sys

if __name__ == '__main__':
    T = sys.stdin.readline()
    for _ in range(int(T)):
        a, b = map(lambda x: int(x), sys.stdin.readline().split(' '))
        print(a+b)

