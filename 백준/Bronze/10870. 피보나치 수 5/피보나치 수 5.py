def p(x):
  if x < 2 : 
    return x 
  else : 
    return p(x-1)+p(x-2)

n=int(input(""))
print(p(n))