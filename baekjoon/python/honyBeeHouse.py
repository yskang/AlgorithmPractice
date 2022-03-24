# Honybee Hoouse
# https://www.acmicpc.net/problem/2292


n = int(input())

i = 1
END = 1

while True:
    if n == 1:
        print(1)
        break
    START = END + 1
    END = START + 6 * i - 1

    if n >= START and n <= END:
        print(i + 1)
        break

    i = i + 1
