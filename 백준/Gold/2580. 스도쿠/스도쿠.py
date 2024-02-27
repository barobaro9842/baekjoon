import sys

board = [[*map(int, sys.stdin.readline().split())] for _ in range(9)]
def check_h(n,i,j):
  if n in board[j] : return False
  return True

def check_v(n,i,j):
  for line in board :
    if n == line[i] : return False
  return True

def check_b(n,i,j):
  for jj in range((j//3)*3,(j//3)*3+3) :
    if n in board[jj][(i//3)*3:(i//3)*3+3] : return False
  return True

def get_possible(i,j):
  poss_set = set([1,2,3,4,5,6,7,8,9]).difference(set(board[j]))
  return list(poss_set)

def get_blank(board):
  a = []
  for j in range(9):
    for i in range(9):
      if board[j][i] == 0:
        a.append((j,i))
  return a

blank = get_blank(board)
catch = 0

def sdoku(depth):
  global catch

  if catch == 1 :
    return
  
  elif depth == len(blank) :
    catch = 1
    for line in board :
      print(" ".join([*map(str, line)]))
    exit()
  
  else :
      j,i = blank[depth]
      idx = 0
      candidates = get_possible(i,j)
      while idx < len(candidates) :
        n = candidates[idx]
        if check_v(n,i,j) and check_b(n,i,j):
          board[j][i] = n
          sdoku(depth+1)
        idx += 1
      board[j][i] = 0
      return False

sdoku(0)