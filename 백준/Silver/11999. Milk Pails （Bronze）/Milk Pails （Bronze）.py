x,y,m = map(int,input().split())
a = m//x + 1
q = []
for i in range(0, a):
  for j in range(a,-1,-1):
    if (x*i)+(y*j) <= m: 
      q.append(x*i + y*j)
print(max(q))