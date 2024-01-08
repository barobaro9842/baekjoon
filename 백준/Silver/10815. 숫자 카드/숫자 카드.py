input()
a = set(map(int, input().split()))
input()
b = [*map(int, input().split())]

for n in b :
  if n in a : print(1, end=" ")
  else : print(0, end=" ")