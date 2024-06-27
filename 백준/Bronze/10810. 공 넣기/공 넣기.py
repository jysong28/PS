n,m=map(int,input().split())
a=[0]*n
for i in range(m):
  x,y,z=map(int,input().split())
  for q in range(x,y+1):
    a[q-1]=z
print(*a)