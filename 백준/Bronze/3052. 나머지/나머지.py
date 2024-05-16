q=0
m=[0] * 42 

for i in range(10):
  a=int(input(""))
  m[a%42] = 1

for j in range(42):
  if m[j]==1:
    q+=1
print(q)
