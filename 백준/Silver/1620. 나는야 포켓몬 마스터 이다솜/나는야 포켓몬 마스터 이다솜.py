import sys

n, m = map(int, sys.stdin.readline().split())
dogam = dict()

for i in range(1,n+1):
  p = sys.stdin.readline().rstrip()
  dogam[p.lower()] = i
  dogam[str(i)] = p

for _ in range(1,m+1):
  t = sys.stdin.readline().rstrip().lower()
  print(dogam[t])
