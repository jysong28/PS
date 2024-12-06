n=int(input())
p=list(map(int,input().split()))
t=0
for i in range(n):
  a=0
  for j in range(i,n):
    if sum(p[i:j+1]) / len(p[i:j+1]) in p[i:j+1]:
      t+=1
print(t)