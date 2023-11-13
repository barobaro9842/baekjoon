def ceil(n):
  if (n*10)%10 == 0 : s = 0
  else : s = 1
  return int((n*10)//10 + s)
  
A,B,V = [*map(int, input().split())]
print(ceil((V-A) / (A-B)) +1)