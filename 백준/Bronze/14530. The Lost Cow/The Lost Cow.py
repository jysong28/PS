x, y = map(int,input().split())

john = x
dis = 1
dir = 1
double = 1
ans = 0

while True:
  for i in range(dis):
    john += dir
    ans += 1
    if john == y:
      print(ans)
      exit()
  double *= 2
  dir *= -1
  dis = abs(john - x) + double 