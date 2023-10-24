import sys
n = int(sys.stdin.readline())
com = [list(sys.stdin.readline().split()) for _ in range(n)]

deque=[]

for i in com:
    lenD = len(deque)
    if i[0] =='push_front':
        deque.insert(0, i[1])
    elif i[0] == 'push_back':
        deque.append(i[1])
    elif i[0] == 'pop_front':
        if lenD == 0:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif i[0] == 'pop_back':
        if lenD == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop(-1)
    elif i[0] == 'size':
        print(lenD)
    elif i[0] == 'empty':
        if lenD == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if lenD == 0:
            print(-1)
        else:
            print(deque[0])
    elif i[0] == 'back':
        if lenD == 0:
            print(-1)
        else:
            print(deque[-1])