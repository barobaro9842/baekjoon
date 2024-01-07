n = int(input())

back = [[0]*100 for _ in range(100)]
for _ in range(n):
  a, b = map(int, input().split())
  for i in range(90-b, 100-b):
    for j in range(a, a+10):
      back[i][j] = 1

res = 0
for i in range(100):
  res += sum(back[i])

print(res)