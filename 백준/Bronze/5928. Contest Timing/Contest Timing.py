d, h, m = map(int,input().split())
d1=((d-11)*60)*24
h1=(h-11)*60
m1=m-11
if d1+h1+m1<0:
  print(-1)
else:
  print(d1+h1+m1)