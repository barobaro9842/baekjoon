import sys

# 괄호 문자열 : (와 )로만 구성되어 있음
# VPS = 올바른 문자열
# "()" = 기본VPS
# 만약 x가 VPS라면, (x)도 VPS
# 두 VPS의 집합도 VPS
# 주어진 문자열이 VPS인지 판단하라

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
  
  string = sys.stdin.readline().rstrip()
  stack = []

  for s in string :
    if s == '(' : stack.append(1)
    elif s == ')' : 
      try : stack.pop()
      except : 
        print('NO')
        break
  else : 
    if len(stack) != 0 : print('NO')
    else : print('YES')
