import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)

N,M = map(int, input().split())
gcd_ = gcd(N,M)
print(gcd_)
print(N*M//gcd_)