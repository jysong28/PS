a=[]
i=0
while True:
  i+=1
  if '666' in str(i):
    a.append(i)
  if len(a)==10000:
    break
n=int(input())
print(a[n-1])