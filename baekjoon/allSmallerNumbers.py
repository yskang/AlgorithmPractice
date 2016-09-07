[numOfInput, n] = list(map(int, input().split(' ')))
print(' '.join(list(map(str, filter(lambda x: x < n, list(map(int, input().split(' '))))))))