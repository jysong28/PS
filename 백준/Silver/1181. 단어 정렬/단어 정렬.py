n=int(input(""))
b=[]
for i in range(n):
  b.append(input())
b=set(b)
b=list(b)
b.sort(key=lambda x:(len(x),x))
for i in range(len(b)):
  print(b[i])