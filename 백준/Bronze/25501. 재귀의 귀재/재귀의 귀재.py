import sys

def recursion(s, l, r, cnt):
  if l >= r : return (1, cnt)
  elif s[l] != s[r] : return (0, cnt)
  else : 
    return recursion(s, l+1, r-1, cnt+1)

def isPalindrom(s):
  l = 0
  r = len(s)-1
  cnt = 1
  return recursion(s,l,r,cnt)

n = int(input())
for _ in range(n):
  s = input()
  print(*isPalindrom(s))