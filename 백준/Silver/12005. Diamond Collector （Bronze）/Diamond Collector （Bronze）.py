n,k = map(int,input().split())
a = []
x = [0]*n
for i in range(n):
  a.append(int(input()))
a.sort()
for i in range(n):
  for j in range(i,n):
    if a[j] - a[i] <= k:
      x[i]+=1
print(max(x))