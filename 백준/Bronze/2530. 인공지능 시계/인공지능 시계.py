a,b,c = map(int,input().split())
d = int(input(""))
a *= 3600
b *= 60
total = a+b+c+d
a = total//3600 % 24
b = total%3600//60
c = total%60
print(a,b,c)