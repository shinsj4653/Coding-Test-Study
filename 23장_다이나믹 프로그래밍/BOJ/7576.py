import sys
input = sys.stdin.readline

# m : 가로칸 수 col, n : 세로칸 수 row
m, n = map(int, input().rstrip().split())
box = []

# 출발 지점이 여러개인 경우!

# 시작지점을 리스트에 넣어놔야 하나??
st = []
alt = []

for i in range(n) :
    row = list(map(int, input().rstrip().split()))
    box.append(row)

    for j in range(m) :
        if box[i][j] == 1 :
            alt.append((i, j))

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :

    while True :

        if len(alt) == 0 :
            break

        while alt:
            st.append(alt.pop())

        while st :
            x, y = st.pop()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m :
                    if box[nx][ny] == 0 :
                        box[nx][ny] = box[x][y] + 1
                        alt.append((nx, ny))
bfs()

answer = 0
isZero = False

for i in range(n) :
    for j in range(m) :
        if box[i][j] == 0 :
            isZero = True
            break
        answer = max(answer, box[i][j])

    if isZero :
        break
if isZero :
    print(-1)
else:
    print(answer - 1)

