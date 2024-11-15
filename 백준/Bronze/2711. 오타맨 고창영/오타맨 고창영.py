a = int(input())
for i in range(a):
  z=[]
  x,y = input().split()
  x = int(x)
  for j in y:
    z.append(j)
  del(z[x-1])
  print("".join(z))