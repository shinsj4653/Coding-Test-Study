# area 변수 전역으로 해도 괜찮나?
# 밑의 코드대로 dfs 형태 짜는 연습 해보기!
# int 형을 return 해주는 dfs 짜는 것이 핵심

import sys
sys.setrecursionlimit(10**5)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# dfs
m, n, k = map(int, input().split())
# m: 세로, n : 가로

g = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k) :
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry) : # 2에서 3
        for x in range(lx, rx) : #0에서 3
            g[m - y - 1][x] = 1 # m : 5, n : 7
#print(g)
areas = []
def dfs(y, x) :
    visited[y][x] = 1
    ret = 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < m and 0 <= nx < n :
            if g[ny][nx] == 0 and not visited[ny][nx] :
                ret += dfs(ny, nx)

    return ret

for y in range(m) :
    for x in range(n) :
        if g[y][x] == 0 and not visited[y][x] :
            areas.append(dfs(y, x))

areas.sort()

print(len(areas))
print(*areas)