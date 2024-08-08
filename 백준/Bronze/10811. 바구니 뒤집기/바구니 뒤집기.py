n,m=map(int,input().split())
b=[]
b1=[]
for p in range(1, n+1):
  b.append(p)
for q in range(m):
  i,j=map(int,input().split())
  b1=b[i-1:j]
  b1.reverse()
  b[i-1:j]=b1
print(*b)