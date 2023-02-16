#7576
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1] #상하좌우
dy = [-1,1,0,0] #상하좌우

M, N = map(int,input().split())

data = list()
for _ in range(N):
    data.append(list(map(int, input().split())))

result = 0

queue = deque([])
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx>=0 and ny>=0 and nx<N and ny<M and data[nx][ny]== 0 :
                data[nx][ny] = data[x][y] + 1
                queue.append([nx,ny])

bfs()
for i in data:
    for j in i :
        if j ==0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)