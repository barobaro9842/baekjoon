import sys

sys.stdin.readline()
a = set([*map(int, input().split())])
b = set([*map(int, input().split())])

res = len(a.difference(b)) + len(b.difference(a))

print(res)