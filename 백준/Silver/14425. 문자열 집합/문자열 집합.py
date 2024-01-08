n,m = map(int,input().split())
s = set()
res = 0

for _ in range(n):
  s.add(input())

for _ in range(m):
  if input() in s : res += 1

print(res)