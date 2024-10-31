n = int(input())
bucket = [0]*1001
for i in range (n):
  s, t, b = map(int,input().split())
  for j in range(s,t):
    bucket[j] += b 
print(max(bucket))