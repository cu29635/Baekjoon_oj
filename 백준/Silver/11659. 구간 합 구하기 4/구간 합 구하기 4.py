#11659
import sys
N, M= map(int, sys.stdin.readline().split())
timea = list(map(int, sys.stdin.readline().split()))
sum_num = []
ssss = 0
for i in range(N):
  ssss = timea[i] + ssss
  sum_num.append(ssss)
    
for _ in range(M):
  s, e = map(int, sys.stdin.readline().split())
  if s==1:
    print(sum_num[e-1])
  else :
    print(sum_num[e-1]-sum_num[s-2])
  