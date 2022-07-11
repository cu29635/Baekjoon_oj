import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)
A, B = map(int, input().split())
print('1'*(gcd(A,B)))