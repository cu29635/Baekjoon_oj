import math
n = int(input())
k = math.factorial(n)
cnt = 0
while(k%10==0):
  cnt += 1
  k //= 10
print(cnt)