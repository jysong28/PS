n=input()
a=[]
for i in range(len(n)):
  a.append(n[i])
a.sort(reverse=True)
for i in range(len(a)):
  print(a[i], end='')