# 꿀팁
# 매개변수로 넘기는 값은 무조건 지역변수로 선언하기!

import sys
sys.setrecursionlimit(10 ** 5)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c, k = map(int, input().split())
m = [list(input()) for _ in range(r)]

v = [[0 for _ in range(c)] for _ in range(r)]

def go(y, x) :
    if y == 0 and x == c - 1 :
        if k == v[y][x] : return 1
        return 0

    ret = 0
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and not v[ny][nx] \
            and m[ny][nx] != 'T' :
            v[ny][nx] = v[y][x] + 1
            ret += go(ny, nx)
            v[ny][nx] = 0
    return ret

v[r - 1][0] = 1
print(go(r - 1, 0))