n=int(input())
t=[0]*1000
a=[]
maxcnt=0
for i in range(n):
  s,e=map(int,input().split())
  a.append([s,e])
  for i in range(s,e):
    t[i]+=1
for i in range(n):
  cnt=0
  for j in range(a[i][0],a[i][1]):
    t[j]-=1
  for k in t:
    if k>0:
      cnt+=1
  maxcnt=max(maxcnt,cnt)
  for l in range(a[i][0],a[i][1]):
    t[l]+=1
print(maxcnt)