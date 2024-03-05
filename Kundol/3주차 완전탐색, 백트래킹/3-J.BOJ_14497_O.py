# 최소 점프 -> bfs
# 2중 for
# *의 상하좌우 -> 만약 상하좌우 0이라면 그 0의 위치에서 상하좌우 dfs?
# -> 1만나는 순간 종료
# -> 계속 이러다가 visited의 배열에서 # 좌표가 1이 되었다 -> 종료

# bfs랑 dfs 혼합?

# 오 맞았다!!! 감격...
from collections import deque

n, m = map(int, input().split())
ret = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y1, x1, y2, x2 = map(int, input().split())
room = [list(input()) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque([(y1 - 1, x1 - 1)])
found = False
def dfs(y, x) :
    global found
    visited[y][x] = 1

    if room[y][x] == '#' :
        found = True
        return

    if room[y][x] == '1' :
        room[y][x] = '0'
        q.append((y, x))
        return

    elif room[y][x] == '0' : # 0이라면
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                dfs(ny, nx)
    return

while q:
    qSize = len(q)

    for s in range(qSize) :

        y, x = q.popleft()

        visited[y][x] = 1

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                dfs(ny, nx)

            if found :
                break
        if found:
            break
    if found:
        break
    ret += 1
print(ret + 1)