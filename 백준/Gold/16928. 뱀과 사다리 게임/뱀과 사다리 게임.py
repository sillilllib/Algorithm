import sys
from collections import deque
input = sys.stdin.readline

board = [0]*101
N, M = map(int, input().split())
ladder = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y 

snake = {} 
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v 

visited = [False]*101
queue = deque([1])
visited[1] = True
while queue:
    x = queue.popleft()
    for i in range(1, 7):
        nx = x+i
        if nx > 100 or visited[nx]:
            continue
        if nx in ladder.keys():
            nx = ladder[nx]
        if nx in snake.keys():
            nx = snake[nx]
        if not visited[nx]:
            queue.append(nx)
            visited[nx] = True
            board[nx] += board[x]+1
print(board[100])