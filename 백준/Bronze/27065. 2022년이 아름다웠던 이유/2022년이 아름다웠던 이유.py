def isPlus(n):
  s = 0
  for i in range(2,n):
    if(n%i==0):
      s = s + i
  return s

a = int(input())

for i in range(a):
  s = 0
  k = 0
  n = int(input())
  for j in range(2,n):
    if(n%j==0):
      s = s + j
      if(isPlus(j)>j):
        print("BOJ 2022")
        k=1
        break
  if(n<s) and k == 0 :
    print("Good Bye")
  elif n>=s and k == 0:
    print("BOJ 2022")