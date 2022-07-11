k = [0,0,0]
while(1):  
  a,b,c = map(int,input().split())
  if(k==[a,b,c]) : break
  if a>b :
    if a>c:
      if(a**2==c**2+b**2): print("right")
      else : print("wrong")
    else :
      if(c**2==a**2+b**2): print("right")
      else : print("wrong")
  else:
    if b>c:
      if(b**2==a**2+c**2): print("right")
      else : print("wrong")
    else :
      if(c**2==a**2+b**2): print("right")
      else : print("wrong")