# 
# https://algospot.com/judge/problem/read/WHITECOLLAR
#

import sys
# import collections
# from collections import defaultdict


testData = [
'5',
'World',
'Algospot',
'Illu',
'Jullu',
'Kodori'
]

testData.reverse()

# rl = lambda: sys.stdin.readline().replace('\n', '').replace('\r', '').strip()
rl = lambda: input()
# rl = lambda: testData.pop()
    
numOfTestCase = int(rl())

for n in range(numOfTestCase):
    line = rl()
    print('Hello, ' + line + '!')

        
            
