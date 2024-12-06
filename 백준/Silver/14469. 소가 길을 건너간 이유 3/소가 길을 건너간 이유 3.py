n=int(input())
t=0
cow=[]
for i in range(n):
  a,e=map(int,input().split())
  cow.append([a,e])
cow.sort()
for i in range(n):
  if t<cow[i][0]:
    t=cow[i][0]
  t+=cow[i][1]
print(t)