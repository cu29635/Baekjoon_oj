def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)

A,B = map(int, input().split())
A2,B2 = map(int, input().split())
gcd_ = gcd(B,B2)
result_A = (A*B2+A2*B)/gcd_
result_B = (B*B2)/gcd_

gcd_result = gcd(result_A,result_B)
print("%d %d" %(result_A/gcd_result,result_B/gcd_result))