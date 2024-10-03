n,k=map(int,input().split())
t=list(map(int,input().split()))
s=[]
for i in range(n-k+1):
  r=0
  for j in range(k):
    r+=t[i+j]
  s.append(r)
print(max(s))