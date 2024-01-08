n = int(input())

arr = [*map(int, input().split())]
a = sorted(set(arr))

dic = dict()
for i,a in enumerate(a):
  dic[a] = i

for i in arr :
  print(dic[i])