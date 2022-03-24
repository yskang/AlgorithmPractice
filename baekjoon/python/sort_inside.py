# https://www.acmicpc.net/problem/1427

def sort_number(n):
    return "".join(sorted(n, reverse=True))


if __name__ == "__main__":
    N = input()
    print(sort_number(N))
