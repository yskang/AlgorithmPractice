# https://algospot.com/judge/problem/read/UBW

import sys

# rl = lambda: sys.stdin.readline().replace('\n', '').replace('\r', '').strip()
# rl = lambda: input()

testData = [
'2',
'11',
'def hello',
' loop 5',
'  world',
'def world',
' loop 2',
'  loop 4',
'   Blade',
'def main',
' loop 3',
'  hello',
'  world',
'3',
'def main',
' loop 5',
' Blade'
]

testData.reverse()

rl = lambda: testData.pop()
numOfTestCase = int(rl())

def executeCode(code):
    functions = {}
    for line in code:
        if line.split(' ')[0] == 'def':
            funcName = line.split(' '[1])
            functions[funcName] = []



    return 0


for n in range(numOfTestCase):
    numOfCode = int(rl())
    code = []
    for i in range(numOfCode):
        code.append(rl())
    
    result = executeCode(code)
    print(result)

            
