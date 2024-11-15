n = int(input())
d = list(map(int,input().split()))
c = list(map(int,input().split()))
price = c[0]
cost = 0
for i in range(len(d)):
  if price > c[i]:
    price = c[i]
  cost += price*d[i]
print(cost)