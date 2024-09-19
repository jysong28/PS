a=input()
a=a.lower()
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t=[0]*26
for i in range(26):
  t[i]=a.count(alp[i])
if t.count(max(t))>1:
  print('?')
else:
  print(alp[t.index(max(t))].upper())