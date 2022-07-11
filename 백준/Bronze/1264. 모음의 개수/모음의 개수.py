while(1):
  arr = input()
  if(arr=='#') : break
  cnt = 0
  arr = arr.lower()
  for i in range(len(arr)):
    if arr[i]=='a' or arr[i]=='e' or arr[i]=='i' or arr[i]=='o' or arr[i]=='u':
      cnt += 1
  print(cnt)