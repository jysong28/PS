m=int(input())
n=int(input())
t=0
min=0

for i in range(1,101):
  for j in range(m,n+1):
    if j==i**2:
      if t==0:
        min=j
      t+=j

if t==0:
  print(-1)
else:
  print(t)
  print(min)