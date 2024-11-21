n = input()
k = n 
m = input()
t = 1
a = 0 
while True:
  if a == len(m):
    break
  if m[a] in k:
    k = n[n.index(m[a])+1:]
  else:
    t += 1
    k = n[n.index(m[a])+1:]
  a+=1
print(t)