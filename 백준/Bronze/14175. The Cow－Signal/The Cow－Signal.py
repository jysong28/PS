m,n,k = map(int,input().split())
string=[]
jiyu=''
for i in range(m):
  a=input('')
  string.append(a)
for i in string:
  jiyu=''
  for j in range(len(i)):
    jiyu+=i[j]*k
  for q in range(k):
    print(jiyu)