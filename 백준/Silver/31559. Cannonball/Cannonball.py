n,s=map(int,input().split())
start=s-1
line=[]
power=1
broken=[]
dir=1
for i in range(n):
  q,v=map(int,input().split())
  line.append((q,v))
for i in range(1000000):
  if start<0 or start>n:
    break
  q,v=line[start]
  if q==0:
    power += v
    dir = dir*-1
  elif q==1:
    if power >= v:
      broken.append(start)

  start+=power*dir
print(len(set(broken)))