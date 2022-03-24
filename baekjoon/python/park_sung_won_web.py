N=int(input())
S=[input()for i in range(N)]
K=int(input())
L=[len(i)for i in S]
S=[int(i)%K for i in S]
p10modK=[1]
for i in range(50):
    p10modK.append((p10modK[i]*10)%K)
DP=[[-1]*(2**16) for i in range(K)]
def pnum(n,d):
    global N,S,K,L,DP,p10modK
    if n==(1<<N)-1:
        DP[d][n]=(d==0)
        return DP[d][n]
    if DP[d][n]>=0:
        return DP[d][n]
    r=0
    for i in range(N):
        if n&(1<<i)!=0:
            continue
        r+=pnum(n+(1<<i),(d*p10modK[L[i]]+S[i])%K)
    DP[d][n]=r
    return DP[d][n]
f=1
for i in range(1,N+1):
    f*=i
gcd=lambda x,y:x if not y else gcd(y,x%y)
a=pnum(0,0)
d=gcd(a,f)
print('%d/%d'%(a//d,f//d))