# 10^2 * 10^4 * 10^4

from collections import defaultdict, deque
r, c, m = map(int, input().split())

# (속력, 방향, 크기)

board = [[0 for _ in range(c)] for _ in range(r)]
shark = defaultdict(int)

for i in range(1, m + 1) :
    sr, sc, s, d, z = map(int, input().split())
    board[sr - 1][sc - 1] = i
    shark[i] = (s, d, z)

#print(board)
#print(shark)

def returnDir(num) :
    if num == 1 :
        return -1, 0

    elif num == 2 :
        return 1, 0

    elif num == 3 :
        return 0, 1

    else :
        return 0, -1


def updateDir(num): # 방향 전환된 dy, dx 를 반환
    if num == 1:
        return 2

    elif num == 2:
        return 1

    elif num == 3:
        return 4

    else:
        return 3

def getNextDirection(i, j, speed, dir) :

    if dir == 1 or dir == 2 : # 위 == 1, 아래 == 2
        # 1 2 3 4 5 6 5 4 3 2
        cycle = r * 2 - 2
        if dir == 1 : # UP
            speed += 2 * (r - 1) - i

        else : # DOWN
            speed += i

        speed %= cycle

        if speed >= r:
            return (2 * r - 2 - speed, j, 1)
        return (speed, j, 2)

    else : # 오른쪽 == 4, 왼쪽 == 3
        cycle = c * 2 - 2
        if dir == 3: # LEFT
            speed += 2 * (c - 1) - j
        else: # RIGHT
            speed += j

        speed %= cycle

        if speed >= c:
            return (i, 2 * c - 2 - speed, 3)
        return (i, speed, 4)


answer = 0
for person in range(c) :

    # 상어 잡기
    for i in range(r) :
        if board[i][person] != 0 :
            key = board[i][person]
            answer += shark[key][2]
            shark.pop(key, None)
            board[i][person] = 0
            break

    # 상어 이동
    next_shark_move = deque() # (상어 키, 이전 y, 다음 x, 다음 y, 다음 x)

    for i in range(r) :
        for j in range(c) :
            if board[i][j] == 0:
                continue

            key = board[i][j]
            speed, direction, size = shark[key]

            # dy, dx = returnDir(direction)
            # sy, sx = i, j # 상어의 업데이트 된 좌표
            #
            # for mo in range(move) :
            #     ny, nx = sy + dy, sx + dx # 다음 갈 좌표
            #
            #     if 0 <= ny < r and 0 <= nx < c :
            #         sy, sx = ny, nx
            #         continue
            #
            #     # 만약 범위 벗어나면 방향 체인지
            #     direction = updateDir(direction)
            #     dy, dx = returnDir(direction)
            #
            #     sy, sx = sy + dy, sx + dx  # 다음 갈 좌표
            #


            sy, sx, newDirection = getNextDirection(i, j, speed, direction)

            newValue = (speed, newDirection, size)
            shark[key] = newValue  # 새로운 방향으로 업데이트

            next_shark_move.append((key, sy, sx))

    # 보드 초기화
    board = [[0 for _ in range(c)] for _ in range(r)]

    # 이동 결과 대로 다음 상어들 배치
    for v in next_shark_move :
        newKey, y, x = v
        #board[oldy][oldx] = 0

        if board[y][x] == 0 :
            board[y][x] = newKey

        else : # 둘 중 큰 놈이 이겨야함, 작은 놈은 잡아먹힘
            preKey = board[y][x]

            if shark[preKey][2] < shark[newKey][2] :
                shark.pop(preKey, None)
                board[y][x] = newKey # 새로운 놈으로 대체

            else :
                shark.pop(newKey, None)


print(answer)