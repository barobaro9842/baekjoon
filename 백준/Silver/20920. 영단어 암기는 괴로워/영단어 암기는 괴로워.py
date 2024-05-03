import sys

n, m = map(int, sys.stdin.readline().split())
words = []
for _ in range(n) :
  temp = sys.stdin.readline().rstrip()
  if len(temp) < m : continue
  else : words.append(temp)

word_dic = dict()
for word in words :
  if word_dic.get(word) == None : word_dic[word] = 1
  else : word_dic[word] += 1

word_set = list(set(words))
word_set.sort()
word_set = sorted(word_set, key=lambda x: len(x), reverse=True)
word_set = sorted(word_set, key=lambda x: word_dic[x], reverse=True)

for word in word_set :
  print(word)