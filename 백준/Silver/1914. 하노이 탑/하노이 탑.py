def rHanoi(n,a,b,c):
  if n==1 :
    print("%c %c" %(a,c))
  else :
    rHanoi(n-1,a,c,b);
    print("%c %c" %(a,c))
    rHanoi(n-1,b,a,c);

n = int(input())
cnt = 2**n -1
print(cnt)
if(n<=20):
  rHanoi(n,'1','2','3')