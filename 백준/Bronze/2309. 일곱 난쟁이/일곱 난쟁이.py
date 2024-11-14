from itertools import combinations

dwarf = []

for i in range(9):
  dwarf.append(int(input()))

for i in combinations(dwarf, 7):
  seven = list(map(int,i))
  if sum(seven) == 100:
    for j in range(7):
      seven.sort()
      print(seven[j])
    break