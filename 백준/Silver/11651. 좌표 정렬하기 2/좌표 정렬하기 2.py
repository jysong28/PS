n = int(input())
c = []
for i in range(n):
  x,y = map(int,input().split())
  c.append([x,y])
c.sort(key = lambda x:(x[1],x[0])) 
for i in range(n):
  print(*c[i])