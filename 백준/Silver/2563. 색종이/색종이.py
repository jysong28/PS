w=[[0]*100 for i in range(100)]
a=int(input(""))
for i in range(a):
  b,c=map(int,input().split())
  for j in range(b,b+10):
    for k in range(c, c+10):
      w[j][k]=1

t=0
for l in range(100):
  t+=w[l].count(1)
print(t)