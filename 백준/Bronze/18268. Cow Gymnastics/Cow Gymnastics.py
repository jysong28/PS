k,n = map(int,input().split())
q = []
for i in range(k):
  a = list(map(int,input().split()))
  q.append(a)

pair = 0 
for i in range(1, n+1):
  for j in range(i+1, n+1):
    cnt=0
    for l in range(k):
      if q[l].index(i) > q[l].index(j):
        cnt +=1
      else:
        cnt -=1
    if abs(cnt) == k:
      pair += 1
print(pair)