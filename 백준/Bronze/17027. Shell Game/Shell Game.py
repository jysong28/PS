N=int(input())
score=[0,0,0]
A=[]
B=[]
G=[]
for i in range(N):
  a,b,g=map(int,input().split())
  A.append(a)
  B.append(b)
  G.append(g)

for i in range(3):
  shell=[0,0,0]
  shell[i]=1
  for j in range(N):
    temp=shell[A[j]-1]
    shell[A[j]-1]=shell[B[j]-1]
    shell[B[j]-1]=temp
    if shell[G[j]-1]==1:
      score[i]+=1
print(max(score))   