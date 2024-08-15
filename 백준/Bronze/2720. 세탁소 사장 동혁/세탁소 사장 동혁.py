n=int(input(""))
for i in range(n):
  t=int(input(""))
  a=t//25
  b=(t-a*25)//10
  c=(t-(a*25+b*10))//5
  d=t-(a*25+b*10+c*5)
  print(a,b,c,d)