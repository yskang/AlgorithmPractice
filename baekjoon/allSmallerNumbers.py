# Numbers that samller than X
# https://www.acmicpc.net/problem/10871

[numOfInput, n] = list(map(int, input().split(' ')))
print(' '.join(list(map(str, filter(lambda x: x < n, list(map(int, input().split(' '))))))))
