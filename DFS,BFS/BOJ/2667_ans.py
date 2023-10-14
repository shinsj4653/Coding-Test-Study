# dfs 하면서 영역의 최대 크기를 어떤식으로 저장하는지 궁금
# -> 전역변수를 사용해서 관리

import sys
input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

danji = []
each = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y) :
    global each
    each += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and chk[nx][ny] == False:
                chk[nx][ny] = True
                dfs(nx, ny)

for i in range(n) :
    for j in range(n) :

        if graph[i][j] == 1 and chk[i][j] == False :
            chk[i][j] = True
            each = 0
            dfs(i, j)
            danji.append(each)

danji.sort()
print(len(danji))
for d in danji :
    print(d)
