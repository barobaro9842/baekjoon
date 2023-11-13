n = int(input())
i = 1
while (i*(i+1)//2 < n):
  i += 1
r = n - i*(i-1)//2
s = i + 1

if s % 2 == 0 : print(f"{s-r}/{r}")
else : print(f"{r}/{s-r}")