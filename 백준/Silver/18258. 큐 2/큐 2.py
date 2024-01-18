import sys
from collections import deque

# 큐 구현
class queue():
  def __init__(self):
    self.q = deque()
  
  def __str__(self):
    return f"{self.q}"
  
  def size(self):
    return len(self.q)
  
  def push(self, x):
    self.q.append(x)

  def pop(self):
    if len(self.q) == 0 : return -1
    else : return self.q.popleft()
  
  def isEmpty(self):
    if len(self.q) == 0 : return 1
    else : return 0
  
  def front(self):
    if len(self.q) != 0 : return self.q[0]
    else : return -1
  
  def back(self) :
    if len(self.q) != 0 : return self.q[-1]
    else : return -1

n = int(sys.stdin.readline().rstrip())
q = queue()

for _ in range(n) :
  command = sys.stdin.readline().rstrip()
  # print(command)
  # print('q:',q)

  if command[:4] == 'push' : q.push(command.split()[1])
  elif command == 'pop' : print(q.pop())
  elif command == 'size' : print(q.size())
  elif command == 'empty' : print(q.isEmpty())
  elif command == 'front' : print(q.front())
  elif command == 'back' : print(q.back())

  # print('-----------')