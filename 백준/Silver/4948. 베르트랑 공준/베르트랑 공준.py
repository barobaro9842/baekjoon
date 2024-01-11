import sys

# n 보다 크고 2n보다 작거나 같은 소수는 무조건 1개 이상잇음
# n이 주어졌을 때, n ~ 2n 사이 소수의 개수는?
# 1 <= n <= 123456

while True :
  n = int(sys.stdin.readline().rstrip())
  if n == 0 : break

  arr = [1]*(2*n+1)
  arr[1] = 0

  for i in range(2, 2*n+1):
    if arr[i] == 0: continue
    else :
      for j in range(2*i, 2*n+1, i):
        arr[j] = 0
  print(sum(arr[n+1:]))