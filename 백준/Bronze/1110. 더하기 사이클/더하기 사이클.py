n = int(input())
k = 0
m=-100000
cnt=0
a = n
while(m!=n):
  if (cnt==0):
    k = a%10 + a//10
    a = a%10
  else :
    temp = k % 10
    k = (a%10 + k%10)
    a = temp
  cnt += 1
  m = a*10 + k%10


print(cnt)