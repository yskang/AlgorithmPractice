n = int(input())

i = 1
end = 1

while True:
    if n == 1:
        print(1)
        break
    start = end + 1
    end = start + 6 * i - 1

    if n >= start and n <= end:
        print(i + 1)
        break

    i = i + 1
