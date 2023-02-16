#7576 토마토
from collections import deque
import sys

dx = [0,0,-1,1,0,0] #상하좌우
dy = [-1,1,0,0,0,0] #상하좌우
dz = [0,0,0,0,-1,1]

M, N, H = map(int,input().split())

arr = list()
for _ in range(H):
    data = list()
    for _ in range(N):
        data.append(list(map(int, input().split())))
    arr.append(data)

#import pdb;pdb.set_trace()
result = 0

queue = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                queue.append([i,j,k])

def bfs():
    while queue:
        z, x, y = queue.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx>=0 and ny>=0 and nz>=0 and nx<N and ny<M and nz<H and arr[nz][nx][ny]== 0 :
                arr[nz][nx][ny] = arr[z][x][y] + 1
                queue.append([nz,nx,ny])

bfs()
for i in arr:
    for j in i :
        for k in j :
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))
print(result-1)