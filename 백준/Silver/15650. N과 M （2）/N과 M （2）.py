import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs  = []
visited = [False] * (N+1)

def recur(num):
    if len(rs) == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(num, N+1):
        if not visited[i]:
            visited[i] = True
            rs.append(i)
            recur(i+1)
            visited[i] = False
            rs.pop()
recur(1)