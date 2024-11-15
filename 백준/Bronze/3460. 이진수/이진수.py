a = int(input())
for i in range(a):
  n = int(input())
  ans = []
  remainder = []
  while n != 0:
    remainder.append(n%2)
    n //= 2
  for i in range(len(remainder)):
    if remainder[i] == 1:
      ans.append(i)
  print(*ans)