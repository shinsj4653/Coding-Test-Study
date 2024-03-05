# 가짓수 -> 완탐
# + 가지치기?
# 일반 dfs + 경로
# k 넘으면 return

# 맞왜틀
# -> 첫 시작점 방문 했다고 해야함!! 주의하도록

import sys
sys.setrecursionlimit(10 ** 5)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c, k = map(int, input().split())
m = [list(input()) for _ in range(r)]

v = [[0 for _ in range(c)] for _ in range(r)]
ret = 0

def dfs(y, x, way) :
    global ret

    if way == k :
        if y == 0 and x == c - 1 :
            ret += 1
        return

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and not v[ny][nx] \
                and m[ny][nx] != 'T' :
            v[ny][nx] = 1
            dfs(ny, nx, way + 1)
            v[ny][nx] = 0

v[r - 1][0] = 1
dfs(r - 1, 0, 1)
print(ret)