import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
  m = int(input())
  c = dict()
  for j in range(m):
    a,b = map(str, input().split())
    
    if b not in c.keys():
      c[b] = 1
    else :
      c[b] += 1
   
  an = 1
  for k in c:
    an *= (c[k]+1)
  print(an-1)