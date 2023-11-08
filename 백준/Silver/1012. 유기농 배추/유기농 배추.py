import sys
sys.setrecursionlimit(10000)
def dfs(x,y):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if not visited[nx][ny] and graph[nx][ny]==1:
                dfs(nx,ny)


T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                count+=1
                
    print(count)
