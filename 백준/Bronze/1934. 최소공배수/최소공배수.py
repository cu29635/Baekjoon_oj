import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)

n = int(input())
for _ in range(n):  
  A, B = map(int, input().split())
  print(A*B//(gcd(A,B)))