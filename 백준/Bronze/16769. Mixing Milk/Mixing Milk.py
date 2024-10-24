bucket = []
for i in range(3):
  x,y = map(int,input().split())
  bucket.append([x,y])

for i in range(33):
  if bucket[0][1] + bucket[1][1] <= bucket[1][0]:
    bucket[1][1] += bucket[0][1]
    bucket[0][1] = 0
  else:
    bucket[0][1] -= (bucket[1][0]-bucket[1][1])
    bucket[1][1] = bucket[1][0]
    
  if bucket[1][1] + bucket[2][1] <= bucket[2][0]:
    bucket[2][1] += bucket[1][1]
    bucket[1][1] = 0
  else:
    bucket[1][1] -= (bucket[2][0]-bucket[2][1])
    bucket[2][1] = bucket[2][0]

  if bucket[2][1] + bucket[0][1] <= bucket[0][0]:
    bucket[0][1] += bucket[2][1]
    bucket[2][1] = 0
  else:
    bucket[2][1] -= (bucket[0][0]-bucket[0][1])
    bucket[0][1] = bucket[0][0]
    
if bucket[0][1] + bucket[1][1] <= bucket[1][0]:
  bucket[1][1] += bucket[0][1]
  bucket[0][1] = 0
else:
  bucket[0][1] -= (bucket[1][0]-bucket[1][1])
  bucket[1][1] = bucket[1][0]

print(bucket[0][1])
print(bucket[1][1])
print(bucket[2][1])