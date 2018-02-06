import sys
from functools import reduce

total_number = int(sys.stdin.readline())
numbers = list(map(lambda x: int(x) ,sys.stdin.readline().replace("\n", "").split(" ")))
max_num = max(numbers)
print(sum(list(map(lambda x: 100*x/max_num, numbers)))/total_number)