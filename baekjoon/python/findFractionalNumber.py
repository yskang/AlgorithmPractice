# Find Fractional Number
# https://www.acmicpc.net/problem/1193

n = int(input())
i = 1

while True:
    sums = int((1 + i) * i * 0.5)
    if sums >= n:
        if (i%2) == 0:
            x = i - (sums - n)
            y = (sums - n) + 1
        else:
            x = (sums - n) + 1
            y = i - (sums - n)

        print(str(x)+'/'+str(y))

        break
    i = i + 1
