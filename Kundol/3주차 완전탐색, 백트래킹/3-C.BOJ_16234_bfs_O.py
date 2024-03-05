from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
area = [[0 for _ in range(n)] for _ in range(n)]
v = [[0 for _ in range(n)] for _ in range(n)]
ret = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def isMove(area) :
    for i in range(n) :
        for j in range(n) :
            if area[i][j] :
                return True

    return False
def bfs(a, b, mark) :
    q = deque([(a, b)])
    flag = False

    while q:
        y, x = q.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n :
                if not v[ny][nx] and l <= abs(land[y][x] - land[ny][nx]) <= r :
                    flag = True
                    v[ny][nx] = 1
                    area[y][x] = mark
                    area[ny][nx] = mark # 영역 색칠
                    q.append((ny, nx))

    if flag :
        return True

    else :
        return False




while True :

    v = [[0 for _ in range(n)] for _ in range(n)]
    area = [[0 for _ in range(n)] for _ in range(n)]
    mark = 1

    for i in range(n) :
        for j in range(n) :
            if not area[i][j] :
                flag = bfs(i, j, mark)
                if flag :
                    mark += 1

   # print(area)
    #print(land)
    # area 배열 모두 0
    # 즉 dfs 한번도 시행 x -> 인구이동 멈춤
    #if not isMove(area):
    if not isMove(area) :
        break

    #print('mark: ', mark)

    # 만약 칠 한 영역 있다면? 인구 이동 시작
    for num in range(1, mark) :
        li = []
        for i in range(n) :
            for j in range(n) :
                if area[i][j] == num :
                    li.append((i, j))

        sum_num = 0
        if len(li) > 0: # li가 없을 수도 있음
            for y, x in li :
                sum_num += land[y][x]

            avg_num = sum_num // len(li)
            for y, x in li :
                land[y][x] = avg_num

    ret += 1

print(ret)