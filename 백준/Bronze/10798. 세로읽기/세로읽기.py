a=[ [""] * 15 for _ in range(5)]


for i in range(5) : 
  tmp = input() 
  for j in range(len(tmp)):
    a[i][j] += tmp[j]

ans = "" 
for i in range(15): 
  for j in range(5) : 
    ans += a[j][i] 

print(ans)