import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(list(map(lambda x: int(x) ,sys.stdin.readline().replace("\n", "").split(" ")))[1:])

for ns in nums:
    average = sum(ns)/len(ns)
    print("%0.3f%%"% (100 * len(list(filter(lambda x: x>average, ns)))/len(ns)))
    

