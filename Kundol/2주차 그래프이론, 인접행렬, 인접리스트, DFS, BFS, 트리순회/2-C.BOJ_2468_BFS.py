# https://ibocon.tistory.com/234
# dy[i] 랑 맨 첫 2중 for문의 i 충돌되어서 오류남
# 변수 겹치지 않게 주의하기

from collections import deque

n = int(input())

ret = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

g = [list(map(int, input().split())) for _ in range(n)]

for num in range(1, 101) :
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n) :
        for j in range(n) :
            if num < g[i][j] and not visited[i][j] :
                q = deque()
                visited[i][j] = True
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            if num < g[nx][ny] and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                cnt += 1

    if cnt == 0:
        break
    elif ret < cnt:
        ret = cnt

print(ret)