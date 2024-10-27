n,k = map(int,input().split())
d = list(map(int,input().split()))

cost = k+1
for i in range(n-1):
  if d[i+1] - d[i] < k + 1:
    cost += d[i+1] - d[i]
  else: 
    cost += k + 1
    
print(cost)