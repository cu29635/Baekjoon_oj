#9613번
import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)
n = int(input())
for _ in range(n):  
  k = list(map(int, input().split()))
  result = 0
  for i in range(1,len(k)):
    for j in range(i+1,len(k)):
      if(i==j): break
      result += gcd(k[i],k[j])
  print(result)