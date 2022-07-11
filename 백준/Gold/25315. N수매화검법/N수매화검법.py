def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
def m_cal(a, b, m):
  if ccw(a[0],a[1],b[0])*ccw(a[0],a[1],b[1]) < 0 and ccw(b[0],b[1],a[0])*ccw(b[0],b[1],a[1]) < 0:
    m = m + 1
  return m
    

cnt = 0
n = int(input())
road = []
for _ in range(n):
  sx, sy, ex, ey, w = map(int, input().split())
  m = 0
  a = [[sx,sy],[ex,ey],w,m]
  road.append(a)
road.sort(key = lambda x:x[2])
for i in range(n):
  for j in range(i+1,n):
    road[i][3] = m_cal(road[i],road[j],road[i][3])
  cnt +=(road[i][3] + 1)*road[i][2]

print(cnt)