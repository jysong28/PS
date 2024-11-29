n,m = map(int,input().split())
spotty = []
plain = []
t = 0

sp = []

for i in range(n):
  genomes = input()
  spotty.append(genomes)
for i in range(n):
  genomes = input()
  plain.append(genomes)

for i in range(m):
  gene = []
  gen = 1
  for j in range(n):
    if spotty[j][i] not in gene:
      gene.append(spotty[j][i])
  for j in range(n):
    if plain[j][i] in gene:
      gen = 0
      break
  t+=gen
print(t)