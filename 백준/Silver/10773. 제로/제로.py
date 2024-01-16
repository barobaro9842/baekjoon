import sys

# 장부 관리
# 실수하면 0을 외침 -> 가장 최근 수를 지움
# 모든 수를 받아적은 후 그 수의 합을 알아보자

# 1<= K <= 10만
# 이후 정수 한개씩
# 정수가 0이면 지울수 있는 정수가 있음

K = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(K):
  n = int(sys.stdin.readline().rstrip())
  if n == 0 : stack.pop()
  else : stack.append(n)

print(sum(stack))