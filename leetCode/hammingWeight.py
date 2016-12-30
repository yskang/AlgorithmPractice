def hammingWeight(n):
    count = 0

    for i in range(31):
        if n & 1 == 1:
            count += 1
        n >>= 1

    return count


print(hammingWeight(15))



