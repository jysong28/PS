members=[]
n=int(input(""))
for i in range(n):
  age, name = input().split()
  members.append([int(age),name])
members.sort(key = lambda x:x[0]) 
for i in range(n):
  print(members[i][0], members[i][1])