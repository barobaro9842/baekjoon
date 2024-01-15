# 1. 일단 N보다 작은 소수를 모두 찾는다.
ckarr = [1] * (1000000+1)
ckarr[0] = ckarr[1] = ckarr[2] = 0
ss = [2]
for i in range(3,len(ckarr),2):
  ckarr[i-1] = 0
  if ckarr[i] == 0 :
    continue
  else :
    ss.append(i)
    for j in range(2*i,len(ckarr),i):
      ckarr[j] = 0

def gold(N):
  bss = []
  for i,s in enumerate(ss) :
    if s > N :
      bss = ss[:i]
      break
  else : bss = ss
  # 2. 골드바흐 파티션을 찾는다.
  # 어떻게 찾을까?
  # 100일 때, [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

  cnt = 0
  li = 0
  ri = len(bss)-1
  while li <= ri :
    r = bss[li] + bss[ri]
    if r == N : 
      cnt += 1
      li += 1
      ri -= 1
    elif r > N :
      ri -= 1
    elif r < N :
      li += 1
  
  print(cnt)

ncase = int(input())
for _ in range(ncase) :
  gold(int(input()))