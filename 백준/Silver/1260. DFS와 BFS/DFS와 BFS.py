from collections import deque

def dfs(start):
    visit_1[start] = 1
    print(start, end= " ")
    
    for i in range(1,N+1):
        if visit_1[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    queue = deque()
    queue.append(start)
    visit_2[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in range(1,N+1):
            if visit_2[i] == 0 and graph[v][i] == 1 :
                visit_2[i]=1
                queue.append(i)
        


N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visit_1 = [0]*(N+1)
visit_2 = [0]*(N+1)

for _ in range(M):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1


dfs(V)
print()
bfs(V)
