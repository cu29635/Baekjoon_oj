
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

m = int(input())
n = int(input())
cnt = 0
s = 0
for i in range(m,n+1):
  if(isPrime(i)):
    if(cnt==0):
      mm = i
    cnt += 1
    s += i

if(cnt==0) :
  print(-1)
else :
  print(s)
  print(mm)
