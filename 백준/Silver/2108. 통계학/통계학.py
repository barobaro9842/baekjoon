import sys

# 산술평균, 중앙값, 최빈값, 범위를 구하라

def mean(arr):
  return round(sum(arr) / len(arr))

def median(arr):
  arr.sort()
  return arr[len(arr)//2]

def mode(arr):
  
  cnt = [0] * 8001
  for a in arr : cnt[a+4000] += 1

  first_i = cnt.index(max(cnt))
  first = cnt[first_i]
  cnt[first_i] = 0
  
  second_i = cnt.index(max(cnt))
  second = cnt[second_i]

  if first == second : return second_i - 4000
  if first > second : return first_i - 4000

def minmaxrange(arr):
  return max(arr) - min(arr)

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))

print(mean(arr))
print(median(arr))
print(mode(arr)) 
print(minmaxrange(arr)) 