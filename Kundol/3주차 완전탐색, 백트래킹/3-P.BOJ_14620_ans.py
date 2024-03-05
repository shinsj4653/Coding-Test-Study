# 정답
#

# 최소 비용
# 얘도 탐색하면서 최소 가격
# -> 최소 넘으면 가지치기 하는 방식으로?

import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
INF = 5000

n = int(input())

a = [list(map(int, input().rstrip().split())) for _ in range(n)]
v = [[0 for _ in range(n)] for _ in range(n)]

ret = INF

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def setFlower(y, x) :
    v[y][x] = 1
    s = a[y][x]
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        v[ny][nx] = 1
        s += a[ny][nx]

    return s
def eraseFlower(y, x) :
    v[y][x] = 0
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        v[ny][nx] = 0

def checkFlower(y, x) : # 하나라도 1있으면 안됨! 모두 0이어야함

    if v[y][x] :
        return False

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n or v[ny][nx] :
            return False

    return True

# cnt가 3일때 꽃 비용 업데이트
def dfs(cnt, hap) :
    global ret

    # 비용 업데이트
    if cnt == 3 :
        ret = min(ret, hap)
        return

    # 꽃 두기
    for i in range(1, n - 1) :
        for j in range(1, n - 1) :
            if checkFlower(i, j) :
                dfs(cnt + 1, hap + setFlower(i, j))
                eraseFlower(i, j)



dfs(0, 0)

print(ret)