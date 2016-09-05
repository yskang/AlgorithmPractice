from functools import reduce

print(reduce(lambda x , y : x + y, [x for x in range(int(input())+1)]))