# Hansoo
# https://www.acmicpc.net/problem/1065

n = int(input())

def isArithmeticSequence(n):
    seq = list(map(int,list(str(n))))
    if len(seq) < 3:
        return True
    a = seq.pop()
    b = seq.pop()
    baseDiff = a - b
    while seq:
        a = seq.pop()
        currDiff = b - a
        if baseDiff != currDiff:
            return False
        b = a
    return True

print(len(list(filter(isArithmeticSequence, [x + 1 for x in range(n)]))))

