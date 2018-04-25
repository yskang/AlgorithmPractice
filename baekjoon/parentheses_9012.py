import sys


def is_valid(parentheses):
    while True:
        temp = parentheses.replace("()", "")
        if temp == parentheses:
            break
        parentheses = temp

    if temp == "":
        return True
    return False


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        parenthesis = sys.stdin.readline().strip()
        if is_valid(parenthesis):
            print("YES")
        else:
            print("NO")
