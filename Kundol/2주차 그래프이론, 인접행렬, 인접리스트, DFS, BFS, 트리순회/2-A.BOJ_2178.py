#https://covenant.tistory.com/141
# -> 공백 없는 맵 입력 방법

from collections import deque

n, m = map(int, input().split())
g = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)] # 방문 여부

q = deque([])
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y, x = 0, 0
visited[y][x] = 1

q.append((x, y))

while q :
    y, x = q.popleft()

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m or g[ny][nx] == 0 :
            continue

        if visited[ny][nx] :
            continue

        visited[ny][nx] = visited[y][x] + 1
        q.append((ny, nx))

print(visited[n - 1][m - 1])