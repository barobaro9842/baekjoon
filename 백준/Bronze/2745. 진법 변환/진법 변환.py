N,B = input().split()
N = list(N)[::-1]
B = int(B)

apb = list('_abcdefghijklmnopqrstuvwxyz'.upper())
res = 0

for i, n in enumerate(N) :
  try : d = int(n) 
  except : d = apb.index(n)+9
  res += d*B**i

print(res)