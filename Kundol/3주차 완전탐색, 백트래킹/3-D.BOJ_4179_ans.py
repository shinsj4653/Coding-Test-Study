# 여러 점 동시에 bfs 하는 로직 공부하기
# 정답
# 최단거리 -> bfs
# 불의 최단거리와 지훈이의 최단거리 비교하기
# 불보다 지훈이가 빠르면 움직일 수 있다

INF = 10e9

from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
q = deque()
ret = 0
fire_check = [[INF for _ in range(c)] for _ in range(r)]
person_check = [[0 for _ in range(c) for _ in range(r)]]
sy, sx = 0, 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def inside(ny, nx) :
    return 0 <= ny < r and 0 <= nx < c


for i in range(r) :
    for j in range(c) :
        if maze[i][j] == 'F' :
            fire_check[i][j] = 1
            q.append((i, j))

        elif maze[i][j] == 'J' :
            sy, sx = i, j


while q :
    y, x = q.popleft()
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if not inside(ny, nx) :
            continue

        if fire_check[ny][nx] != INF or maze[ny][nx] == '#' :
            continue

        fire_check[ny][nx] = fire_check[y][x] + 1
        q.append((ny, nx))

person_check[sy][sx] = 1 # 'J' 시작위치
q.append((sy, sx))

while q :
    y, x = q.popleft()

    if y == 0 or y == r - 1 or x == 0 or x == c - 1 :
        ret = person_check[y][x]
        break

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if not inside(ny, nx) :
            continue

        if person_check[ny][nx] or maze[ny][nx] == '#' :
            continue

        if fire_check[ny][nx] <= person_check[y][x] + 1 :
            continue

        person_check[ny][nx] = person_check[ny][nx] + 1
        q.append((ny, nx))

if ret != 0 :
    print(ret)

else :
    print('IMPOSSIBLE')


