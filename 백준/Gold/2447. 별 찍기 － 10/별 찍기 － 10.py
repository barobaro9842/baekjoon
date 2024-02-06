import sys

def star_pattern(start_i, start_j, n) :
  if n != 1 :
    for i in range(start_i, start_i+n):
      if start_i+n//3 <= i and i < start_i+n//3*2:
        for j in range(start_j+n//3,start_j+n//3*2) :
          star[i][j] = " "

    for r in [0, n//3, n//3*2]:
      for c in [0, n//3, n//3*2]:
        star_pattern(start_i+r, start_j+c, n//3)

        

n = int(sys.stdin.readline())
star = []
for _ in range(n) :
  star.append(["*"] * n)

star_pattern(0, 0, n)
for i in range(n) :
  for j in range(n) :
    print(star[i][j], end="")
  print()