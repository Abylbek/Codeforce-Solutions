n=int(input())
L=list(map(int,input().split()))
X=[0]*(n+1)
for i in range(n):
    X[L[i]]=i+1
v,p=0,0
m=int(input())
M=list(map(int,input().split()))
for x in M:
    v+=X[x]
    p+=n-X[x]+1
print(v,p) 