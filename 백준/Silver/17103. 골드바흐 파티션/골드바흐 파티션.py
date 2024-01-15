maxn = 1000001
ck = [1] * maxn
ck[0] = ck[1] = 0
s = []
for i in range(2,maxn) :
  if ck[i] == 0 : continue
  else :
    s.append(i)
    for j in range(i*2, maxn, i): 
      ck[j] = 0

ncase = int(input())
for _ in range(ncase) :
  N = int(input())
  cnt = 0
  for i in s :
    if i > N//2 : break
    if ck[N-i] == 1 : cnt += 1

  print(cnt)