N=int(input(""))
m=list(map(int,input().split()))
m.sort()
t=0 
q=0
for i in range(N):
  t+=m[i]
  q+=t
print(q)