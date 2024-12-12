n=int(input())
q=input()
value=[]
maxv = 1
for i in range(n):
    for j in range(i+1,n+1):
        a = q[i:j]
        b = q.find(a) + 1
        if (q.find(a, b) == -1):
            maxv = max(maxv, len(a))
            break
print(maxv)