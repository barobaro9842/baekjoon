n = int(input())
m = int(input())

a = [1] * (m+1)
res = []

for i in range(2,m+1):
  if a[i] != 1: continue
  else :
    if i >= n : res.append(i)

  for j in range(i,m+1,i):
    a[j] = 0

if res != [] :
  print(sum(res))
  print(min(res))
else :
  print("-1")