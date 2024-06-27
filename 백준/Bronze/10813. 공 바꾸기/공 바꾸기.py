n,m=map(int,input().split())
q=[]
for wee in range(1,n+1):
  q.append(wee)
for p in range(m):
  i,j=map(int,input().split())
  q[i-1],q[j-1]=q[j-1],q[i-1]
print(*q)