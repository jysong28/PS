n,k=map(int,input().split())
coin = [] 
t=0
for i in range(n):
  coin.append(int(input("")))

coin.sort(reverse = True) # 내림차순으로 정렬 
for j in coin: 
  t+=k//j
  k %= j #k=k-((k//j)*j)

print(t)