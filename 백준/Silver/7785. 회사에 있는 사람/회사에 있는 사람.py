res = set()
n = int(input())

for _ in range(n):
  p, e = input().split()
  if e == "enter" : res.add(p)
  else : res.remove(p)

for p in sorted(res, reverse=True):
  print(p)