check  = [0 for _ in range(30)] 
 
for i in range(28):
  a=int(input(""))
  check[a-1]=a

for j in range(30):
  if check[j]==0:print(j+1)