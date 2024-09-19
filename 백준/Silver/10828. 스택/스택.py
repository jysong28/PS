s=[]
for i in range(int(input())):
  c=input().split()
  if c[0]=='push':
    s.append(c[1])
  elif c[0]=='pop':
      print(s.pop() if len(s)>0 else -1)
  elif c[0]=='size':
    print(len(s))
  elif c[0]=='empty':
    print(int(len(s)==0))
  elif c[0]=='top':
    print(s[-1] if len(s)>0 else -1)