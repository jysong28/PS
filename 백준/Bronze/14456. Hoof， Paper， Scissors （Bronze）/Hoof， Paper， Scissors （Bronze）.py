n=int(input())
m=[0,0]

for i in range(n):
    a,b=map(int,input().split())
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        m[0]+=1 
    elif (a==1 and b==3) or (a==3 and b==2) or (a==2 and b==1):
        m[1]+=1 
print(max(m))