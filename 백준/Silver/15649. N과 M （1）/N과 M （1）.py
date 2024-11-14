from itertools import permutations

k = []
a,b = map(int,input().split())
for i in range(1,a+1):
  k.append(i)
for i in permutations(k,b):
  print(*i)