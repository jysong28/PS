n = int(input())
remainder = []
while n != 0:
  remainder.append(n%2)
  n //= 2
remainder.reverse()
remainder = list(map(str,remainder))
print("".join(remainder))