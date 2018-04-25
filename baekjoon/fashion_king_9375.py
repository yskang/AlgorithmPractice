import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n = int(sys.stdin.readline().strip())

        items = {}

        for _ in range(n):
            wear, pos = sys.stdin.readline().strip().split(' ')

            if pos in items:
                items[pos] += 1
            else:
                items[pos] = 2

        max_case = 1
        for pos in items:
            max_case = max_case * items[pos]

        print(max_case-1)
