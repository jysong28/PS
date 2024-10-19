
import sys 
n,q=map(int,sys.stdin.readline().split())
c=list(map(int,sys.stdin.readline().split()))
t=list(map(int,sys.stdin.readline().split()))

apple=[]
for i in range(len(c)):
  apple.append(c[i] - t[i])
apple.sort(reverse=True)

for i in range(q):
  v,s=map(int,sys.stdin.readline().split())
  if apple[v-1]>s:
    print("YES")
  else: 
    print('NO')