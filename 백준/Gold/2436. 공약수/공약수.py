import math
import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)
A, B = map(int, input().split())

min_div = B//A
for i in range(1,int(math.sqrt(min_div))+1):
  if(min_div%i==0):
    a = i
    b = min_div//i
    if(gcd(a,b)==1):
      result_a = a
      result_b = b

print("%d %d" %(result_a*A, result_b*A))