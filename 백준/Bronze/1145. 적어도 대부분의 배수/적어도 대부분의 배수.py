i=1
t=0
a=list(map(int,input().split()))
while True:
  t=0
  for j in a:
    if i%j==0:
      t+=1
  if t>=3:
    print(i)
    break
  i+=1