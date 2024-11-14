from itertools import combinations

k = []
a,b = map(int,input().split())
for i in range(1,a+1):
  k.append(i)
for i in combinations(k,b):
  print(*i)