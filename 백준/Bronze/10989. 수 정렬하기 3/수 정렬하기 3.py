import sys 
input = sys.stdin.readline

n = int(input())
l = [0]*10001
for i in range(n):
  a = int(input())
  l[a] += 1
for i in range(1,len(l)):
  if l[i] != 0:
    for j in range(l[i]):
      print(i)