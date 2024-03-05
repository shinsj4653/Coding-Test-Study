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

def getPrice() :
    price = 0
    for i in range(n) :
        for j in range(n) :
            if v[i][j] :
                price += a[i][j]
    return price

def checkFlower(y, x) : # 하나라도 1있으면 안됨! 모두 0이어야함
    return v[y][x] or v[y - 1][x] or v[y + 1][x] \
or v[y][x + 1] or v[y][x - 1]

# cnt가 3일때 꽃 비용 업데이트
def dfs(cnt) :
    global ret

    # 비용 업데이트
    if cnt == 3 :
        price = getPrice()

        if price < ret :
            ret = price

        return


    # 꽃 두기
    for i in range(1, n - 1) :
        for j in range(1, n - 1) :
            if not checkFlower(i, j) :
                v[i][j] = 1
                v[i - 1][j] = 1
                v[i + 1][j] = 1
                v[i][j - 1] = 1
                v[i][j + 1] = 1

                dfs(cnt + 1)

                v[i][j] = 0
                v[i - 1][j] = 0
                v[i + 1][j] = 0
                v[i][j - 1] = 0
                v[i][j + 1] = 0


dfs(0)

print(ret)