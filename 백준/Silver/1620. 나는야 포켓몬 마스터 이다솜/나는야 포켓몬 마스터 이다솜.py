import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = list(input().strip() for _ in range(n))

for i in range(m):
  a = input().strip()
  if(a.isdigit()):
    print(d[int(a)-1])
  else :
    print(d.index(a)+1)