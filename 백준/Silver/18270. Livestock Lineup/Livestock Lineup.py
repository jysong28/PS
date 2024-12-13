from itertools import permutations
n=int(input())
a=[]
cow=['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
for i in range(n):
    s=input().split()
    a.append([s[0],s[-1]])
cow.sort()
cows=list(permutations(cow,8))
for i in cows:
    check = True 
    for j in range(n):
        if abs(i.index(a[j][0])-i.index(a[j][1]))==1:
            pass
        else:
            check = False 
    if check == True: 
        print(*i,sep="\n")
        break