import math
A, B = map(int, input().split())
result = [True] * (B-A+1)
b = int(B**0.5)

for i in range(2,b+1):
  v = i*i
  for j in range(A//v*v, B+1, v):
    if(j-A>=0):
      result[j-A] = False
print(result.count(True))