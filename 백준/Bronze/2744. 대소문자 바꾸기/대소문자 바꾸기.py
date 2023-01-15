arr = input()
ar2 = ''
for j in arr:
  if j.isupper():
    ar2 =  ar2 + j.lower()
  else :
    ar2 = ar2 + j.upper()
print(ar2)