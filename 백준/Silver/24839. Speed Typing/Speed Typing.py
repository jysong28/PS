n = int(input())
results = []

for _ in range(n):
    c1 = input()
    c2 = input()

    i, j = 0, 0
    while i < len(c1) and j < len(c2):
        if c1[i] == c2[j]:
            i += 1
        j += 1

    if i == len(c1):
        results.append(len(c2) - len(c1))
    else:
        results.append('IMPOSSIBLE')

l = 1
for i in results:
    print(f'Case #{l}: {i}')
    l += 1 