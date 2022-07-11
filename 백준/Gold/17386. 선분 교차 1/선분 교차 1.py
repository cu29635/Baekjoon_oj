import sys
def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
a = [x1,y1]
b = [x2,y2]
c = [x3,y3]
d = [x4,y4]

if ccw(a,b,c)*ccw(a,b,d) < 0 and ccw(c,d,a)*ccw(c,d,b) < 0:
  print(1)
else :
  print(0)