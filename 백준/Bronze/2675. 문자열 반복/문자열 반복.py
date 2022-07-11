n = int(input())
for _ in range(n):
  k, arr = input().split()
  st =str()
  for i in range(len(arr)):
    st = st + arr[i]*int(k)
  print(st)