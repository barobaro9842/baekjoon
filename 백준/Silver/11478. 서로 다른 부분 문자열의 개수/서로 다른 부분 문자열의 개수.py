import sys

# 문자열 S
# 서로 다른 부분 문자열의 개수
# 길이 <= 1000

s = input()
l = len(s)
res = set()

for i in range(0,l+1):
  for j in range(i+1,l+1):
    res.add(s[i:j])

print(len(res))