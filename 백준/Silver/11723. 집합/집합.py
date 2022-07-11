import sys
s = set()
n = int(sys.stdin.readline())
for _ in range(n):
  arr = sys.stdin.readline().split()
  if(arr[0]=="add"):
    s.add(int(arr[1]))
  elif(arr[0]=="remove"):
    s.discard(int(arr[1]))
  elif(arr[0]=="check"):
    if int(arr[1]) in s:
      print(1)
    else : print(0)
  elif(arr[0]=="toggle"):
    if int(arr[1]) in s:
      s.discard(int(arr[1]))
    else :
       s.add(int(arr[1]))
  elif(arr[0]=="all"):
    s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  elif(arr[0]=="empty"):
    s = set()