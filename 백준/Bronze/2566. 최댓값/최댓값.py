t= [list(map(int,input().split())) for i in range(9)]
m=0
x=0
y=0
for i in range(len(t)):
  for j in range(len(t[i])):
    if t[i][j]>=m:
      m=t[i][j]
      x=i+1
      y=j+1
print(m)
print(x, y)