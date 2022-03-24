import sys
from functools import reduce
print(reduce(lambda x, y: x+y+"\n" if len(list(filter(lambda k: k is not "\n",x+y)))%10 is 0 else x+y , sys.stdin.readline()))
