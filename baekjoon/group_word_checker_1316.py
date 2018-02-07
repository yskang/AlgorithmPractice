# https://www.acmicpc.net/problem/1316
import sys


def is_group_word(word):
    a = "abcdefghijklmnopqrstuvwxyz"
    dic = {x:False for x in a}
    word += "0"
    prev = word[0]
    for current in word[1:]:
        if prev != current:
            if dic[prev]:
                return False
            else:
                dic[prev] = True
        prev = current

    return True

if __name__ == "__main__":
    N = int(input())
    count = 0
    for i in range(N):
        word = sys.stdin.readline().strip()
        if is_group_word(word):
            count += 1
    print(count)
