p = [0]*10
for i in range(10):
  a, b = map(int,input().split())
  p[i]-=a
  p[i]+=b
  if i<9:
    p[i+1] = p[i]
print(max(p))