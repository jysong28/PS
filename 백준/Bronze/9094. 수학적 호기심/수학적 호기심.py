q=int(input(""))
for i in range(q):
  t=0
  n,m=map(int,input().split())
  for a in range(1,n):
    for b in range(a+1,n):
      if (a**2+b**2+m)%(a*b)==0:
        t+=1
  print(t)