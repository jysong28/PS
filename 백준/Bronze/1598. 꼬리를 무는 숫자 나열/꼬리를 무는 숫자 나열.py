import sys 

input=sys.stdin.readline

a,b=map(int,input().split())
h=abs((b-1)//4 - (a-1)//4)
v=abs((b-1)%4 - (a-1)%4)

print(h+v)