from math import *

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

for i in range(n):
  s = isqrt(a[i]*b[i])
  if a[i]*b[i] == s*s :
    temp = a[i]
    a[i] = b[i]
    b[i] = temp
if(a==sorted(a)) : print("YES")
else : print("NO")