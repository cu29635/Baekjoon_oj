a = list(map(int, input().split()))
b = sorted(a)
c = sorted(a)
c.sort(reverse=True)
if(a==b):
  print('ascending')
elif (a==c):
  print('descending')
else :
  print('mixed')