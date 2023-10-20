import sys
from collections import deque

input = sys.stdin.readline

# 4, 6
n, m = map(int, input().split())

maze = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
chk = [[False for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n) : # 0 ~ 3
    row = input()

    for j in range(m) : # 0 ~ 5
        maze[i + 1][j + 1] = int(row[j])

#print(maze)
answer = 0

dx = [-1, 1, 0, 0] # 북, 남, 동, 서
dy = [0, 0, 1, -1]

stack = []

def bfs(x, y) :
    queue = deque([(x, y)])
    chk[x][y] = True

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= m :
                if maze[nx][ny] == 1 and chk[nx][ny] == False :
                    maze[nx][ny] += (maze[x][y])
                    queue.append((nx, ny))
bfs(1, 1)
print(maze[n][m])




