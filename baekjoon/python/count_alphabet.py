W = input()
L = list(W.upper())

M = []
count = 0
C = []
last = 0
M.append(L[0])    
C.append(0)

for i in range(len(L)):     #알파벳 갯수 세기
    for j in range(len(M)):
        count = C[j]
        if M[j] == L[i]:
           count += 1
           C.pop(j)
           C.insert(j,count)
           break
        elif (M[j] != L[i]) and (j+1!=len(M)):
            pass
        elif (M[j] != L[i])and (j+1==len(M)):
            M.append(L[i])
            count = 1
            C.append(count)
            last += 1
            break
        
Max = C[0]
count = 0
j = 0
for i in range(1,len(C)):   #'?'인지 아닌지 판별을 위함
    if Max > C[i]:
        pass
    elif Max == C[i]:
        count += 1
    else:
        Max = C[i]
        j = i
        count = 0
        
    
if count != 0:
    print('?')
else:
    print(M[j])
