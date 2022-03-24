# Repeat String
# https://www.acmicpc.net/problem/2675

numOfTest = int(input())

for test in range(numOfTest):
    [n, letters] = input().split(' ')
    
    result = []
    for letter in letters:
        for i in range(int(n)):
            result.append(letter)

    print(''.join(result))
        

