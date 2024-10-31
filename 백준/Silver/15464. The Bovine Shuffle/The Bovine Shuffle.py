n = int(input())
a = list(map(int,input().split()))
q = 0
id = list(map(int,input().split()))
id2 = []
for i in range(3):
  id2 = []
  for j in range(n):
    id2.append(id[a[j]-1])
  id=id2[:]

for i in range(n):
  print(id2[i])