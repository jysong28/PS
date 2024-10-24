a = []
n = int(input(""))
for i in range(n):
  p = int(input(""))
  a.append(p)
a.sort()
for i in range(len(a)):
  print(a[i])