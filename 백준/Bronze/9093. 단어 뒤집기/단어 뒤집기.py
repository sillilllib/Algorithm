n = int(input())
for i in range(n):
    w = list(input().split())
    for j in w:
        print(j [::-1], end=' ')