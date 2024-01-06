n, b = map(int, input().split())
a = list('0123456789abcdefghijklmnopqrstuvwxyz'.upper())
res = ''

while (n>0):
  r = n % b
  n = n // b
  res = res + a[r]

print(res[::-1])