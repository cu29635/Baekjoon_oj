import sys
def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
a = [x1,y1]
b = [x2,y2]
c = [x3,y3]
d = [x4,y4]

if ccw(a,b,c)*ccw(a,b,d) <= 0 and ccw(c,d,a)*ccw(c,d,b) <= 0:
  if ccw(a,b,c)*ccw(a,b,d) == 0 and ccw(c,d,a)*ccw(c,d,b) == 0:
    if (max(a[0],b[0]) >= min(c[0],d[0]) and 
        max(c[0],d[0]) >= min(a[0],b[0])) and (max(a[1],b[1]) >= min(c[1],d[1]) and 
        max(c[1],d[1]) >= min(a[1],b[1])):
        print(1)
    else :
      print(0)
  else :
    print(1)
else :
  print(0)