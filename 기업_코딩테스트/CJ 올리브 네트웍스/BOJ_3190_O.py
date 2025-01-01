# . . . . . .
# . . . . o .
# . . . o . .
# . . . . . .
# . . o . . .
# . . . . . .
from collections import deque

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)] # 뱀 : 1

t = 0 # 시작 시간
sy, sx = 0, 0 # 시작 y, x (머리)
taily, tailx = sy, sx # 꼬리 y, x

board[sy][sx] = 1

k = int(input())
for i in range(k) :
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2 # 사과 2

dy = 0
dx = 1 # 맨 처음엔 오른쪽으로 이동

l = int(input())
d_li = deque()
for i in range(l) :
    time, direction = input().rstrip().split()
    time = int(time)

    d_li.append((time, direction))

#print(d_li)
d_hist = deque()
def updateDir(y, x, d) :
    if d == 'L' :
        # 전 방향이 오른쪽
        if y == 0 and x == 1 :
            return -1, 0 # 이젠 위쪽
        # 전 방향이 아래쪽
        elif y == 1 and x == 0 :
            return 0, 1 # 이젠 오른쪽
        # 전 방향이 왼쪽
        elif y == 0 and x == -1 :
            return 1, 0 # 이젠 아래쪽
        # 전 방향이 위쪽
        elif y == -1 and x == 0 :
            return 0, -1 # 이젠 왼쪽

    else :
        # 전 방향이 오른쪽
        if y == 0 and x == 1:
            return 1, 0  # 이젠 아래쪽
        # 전 방향이 아래쪽
        elif y == 1 and x == 0:
            return 0, -1  # 이젠 왼쪽
        # 전 방향이 왼쪽
        elif y == 0 and x == -1:
            return -1, 0  # 이젠 위쪽
        # 전 방향이 위쪽
        elif y == -1 and x == 0:
            return 0, 1  # 이젠 오른쪽

while(True) :
    # 시간 증가
    t += 1

    # 다음에 갈 좌표
    ny = sy + dy
    nx = sx + dx

    # 벽에 부딪히는지 체크
    if ny < 0 or ny >= n or nx < 0 or nx >= n :
        print(t)
        break

    # 자기자신이랑 부딪히는지 체크
    if board[ny][nx] == 1 :
        print(t)
        break

    # 머리의 이동 히스토리 기록 -> 꼬리를 위해
    d_hist.append((dy, dx))

    # 뱀 몸길이 늘려 머리를 다음 칸에 위치
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[ny][nx] == 2 :
        board[ny][nx] = 1

    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else :
        board[ny][nx] = 1
        board[taily][tailx] = 0

        histy, histx = d_hist.popleft()
        taily += histy
        tailx += histx

    # 방향 바꿔야 하는 경우
    if d_li and t == d_li[0][0] :
        tt, d = d_li.popleft() # 시간, 방향
        dy, dx = updateDir(dy, dx, d)

    sy, sx = ny, nx
