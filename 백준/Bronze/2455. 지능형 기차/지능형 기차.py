a=[0]*4
m=0
for i in range(4):
  n,m=map(int,input().split())
  a[i]=a[i-1]+(m-n)
print(max(a))