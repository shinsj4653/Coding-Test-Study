# 사각 지대의 최소 크기

# 1번 : 4방향
# 2번 : 2방향
# 3번 : 4방향
# 4번 : 4방향
# 5번 : 1방향

# 백트래킹은 맞는 것 같긴한데..
# 카메라 당 방향이 너무 많은데..
# 진법 사용 -> 4진법!


import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board1 = [] # 사무실
board2 = [] # cctv 방향 정한 후에 cctv의 감시 영역에 걸리는 빈칸은 값을 7로 바꾸는 작업
cctv = [] # cctv의 좌표들을 ㄷ마을 변수

# for i in range(n) :
#     board1.append(list(map(int, input().split())))
#
# print(board1)

# 남, 동, 북, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def oob(a, b) : # (a, b) 가 범위를 벗어났는지 체크하는 함수
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x, y, dir) : # dir 방향으로 진행하면서 벽을 만날 때 까지 지나치는 모든 빈 칸을 7로 바꿈
    dir = int(dir % 4)
    while True : 
        x += dx[dir]
        y += dy[dir]
        if oob(x, y) or board2[x][y] == 6 : # 범위 벗어나거나, 벽일때 -> cctv 탐색 끝
            return 
        
        if board2[x][y] != 0 : # 만약 0이 아닌 경우 -> cctv인 경우는 지나칠 수 있음!
            continue
            
        board2[x][y] = 7
        
mn = 0 # 사각 지대의 최소 크기 저장할 변수

# 초기 mn 세팅
for i in range(n) :
    row = list(map(int, input().split()))
    row2 = []

    for j in range(m) :
        if row[j] != 0 or row[j] != 6 :
            cctv.append((i, j))

        if row[j] == 0 :
            mn += 1

        row.append(0)

    board1.append(row)
    board2.append(row)

for tmp in range(4 ** len(cctv)) :
    for i in range(n) :
        for j in range(m) :
            board2[i][j] = board1[i][j]
    brute = tmp
    for i in range(len(cctv)) :
        dir = int(brute % 4)
        brute /= 4
        x, y = cctv[i]

        if board1[x][y] == 1 :
            upd(x, y, dir)

        elif board1[x][y] == 2 :
            upd(x, y, dir)
            upd(x, y, dir + 2)

        elif board1[x][y] == 3 :
            upd(x, y, dir)
            upd(x, y, dir + 1)

        elif board1[x][y] == 4 :
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)

        else : # board1[x][y] == 5
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)

        val = 0
        for i in range(n) :
            for j in range(m) :
                if board2[i][j] == 0 :
                    val += 1

        mn = min(mn, val)

print(mn)

        



