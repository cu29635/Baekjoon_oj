import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)

n = int(input())
for _ in range(n):  
  k = list(map(int, input().split()))
  max_list = []
  for i in range(len(k)):
    for j in range(i+1,len(k)):
      if(i==j): break
      max_list.append(gcd(k[i],k[j]))
  print(max(max_list))