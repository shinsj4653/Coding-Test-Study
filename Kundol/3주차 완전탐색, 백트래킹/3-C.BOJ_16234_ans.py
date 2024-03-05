# 야매 풀이인 것 같아 정답 보고 다시 복습
# 1. 아예 bfs 에서 인구이동 일어났나 인일어났다 판단해도 될듯
# -> isMove() 함수 필요 없어짐!

# 2. visited랑 좌표 배열만 이용해서 구할 수도 있다!
# -> 각 탐색마다 인구 이동 로직까지 실행 가능

from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
v = []
ret = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
sum_num = 0
def bfs(a, b, v) :
    global sum_num
    q = deque([(a, b)])
    while q:
        y, x = q.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n :
                if not visited[ny][nx] and l <= abs(land[y][x] - land[ny][nx]) <= r :
                    visited[ny][nx] = 1
                    v.append((ny, nx))
                    sum_num += land[ny][nx]
                    q.append((ny, nx))


while True :
    #mark = 1
    flag = False

    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                v.clear()
                visited[i][j] = 1
                v.append((i, j))
                sum_num = land[i][j]
                bfs(i, j, v)

                if len(v) == 1 : # 인구 이동 안한 경우
                    continue

                for y, x in v : # 인구 이동 시작
                    land[y][x] = sum_num // len(v)
                    flag = True


    # bfs 단 한 번도 시행 안되면 flag == False
    if not flag :
        break

    ret += 1

print(ret)