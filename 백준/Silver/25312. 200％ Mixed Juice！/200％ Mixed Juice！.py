import sys
sys.setrecursionlimit(10000)

def gcd(a, b):
  if(a%b==0) : return b
  else : return gcd(b,a%b)

N,M = map(int, input().split())

result_list=[]
result_a = 0
result_b = 1
for i in range(N):
  w,v = map(int, input().split())
  list_ = [v/w,v,w]
  result_list.append(list_)
result_list.sort(key= lambda x:x[0], reverse=True)
for i in range(N) :
  gcd_b = gcd(result_b,result_list[i][2])
  if(M>=result_list[i][2]) : 
    M = M - result_list[i][2]
    result_a = (result_list[i][1]*result_list[i][2]*result_b+result_a*result_list[i][2])/gcd_b
    result_b = result_b*result_list[i][2]/gcd_b
  else :
    result_a = (result_list[i][1]*result_b*M+result_a*result_list[i][2])/gcd_b
    result_b = result_b*result_list[i][2]/gcd_b
    M = 0
  gcd_ = gcd(result_a,result_b)
  result_a = result_a/gcd_
  result_b = result_b/gcd_
  if(M==0) : break
  
print("%d/%d" %(result_a,result_b))