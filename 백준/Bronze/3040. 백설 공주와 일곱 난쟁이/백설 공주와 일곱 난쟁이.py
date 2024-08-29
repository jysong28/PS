baeksul=[]
dwarf=0
for i in range(9):
  a=int(input(""))
  baeksul.append(a)
  dwarf+=a

dwarf-=100

for k in range(9):
  for l in range(k+1,9):
    if baeksul[k]+baeksul[l]==dwarf:
      qwe=baeksul[k]
      qweq=baeksul[l]
      
baeksul.remove(qwe)
baeksul.remove(qweq)
for werwer in range(len(baeksul)):
  print(baeksul[werwer])