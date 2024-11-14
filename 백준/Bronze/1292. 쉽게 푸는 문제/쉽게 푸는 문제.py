n = []
t=0
for i in range(46):
  for j in range(i):
    n.append(i)
a,b = map(int,input().split())
for i in range(a,b+1):
  t+=n[i-1]
print(t)