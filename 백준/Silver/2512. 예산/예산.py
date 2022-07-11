N = int(input())
money = list(map(int, input().split()))
money.sort()
max_money = int(input())
start = 0
end = max(money)

while start<=end:
  mid = (start+end)//2
  result = 0
  for m in money :
    if(mid>m):
      result +=m
    else :
      result += mid
  if max_money>=result:
    start = mid + 1
  else :
    end = mid - 1
print(end)