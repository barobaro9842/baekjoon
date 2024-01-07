r = [['_']*5 for _ in range(15)]

for i in range(5):
  tmp = list(input())
  for j in range(len(tmp)):
    r[j][i] = tmp[j]

for n in r :
  for a in n :
    if a != "_" : print(a, end='')