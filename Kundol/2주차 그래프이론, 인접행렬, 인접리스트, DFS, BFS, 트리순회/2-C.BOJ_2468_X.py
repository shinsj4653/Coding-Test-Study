import sys
sys.setrecursionlimit(100000)

# 메모리 초과 문제 뜸
# visited 하나만 생성하고 0으로 값 초기화 해주는 방법도 안 먹힘..
# visited 매개변수로 주지도 않았는데 또 메모리 초과 뜸..
# -> bfs로 풀면 해결된다.

n = int(input())
visited = [[0 for _ in range(n)] for _ in range(n)]

min_num, max_num = 101, 2
g = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(n) :
    l = list(map(int, input().split()))
    # mi = min(l)
    # ma = max(l)
    #
    # if min_num > mi :
    #     min_num = mi
    #
    # if max_num < ma :
    #     max_num = ma

    g.append(l)

ret = 1
def dfs(y, x, num) :

    visited[y][x] = 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue

        if g[ny][nx] > num and visited[ny][nx] == 0 :
            dfs(ny, nx, num)

    return

for num in range(2, 101) :
    cnt = 0

    for y in range(n) :
        for x in range(n) :
            if g[y][x] > num and visited[y][x] == 0 :
                dfs(y, x, num)
                cnt += 1

    ret = max(ret, cnt)

    for i in range(n) :
        for j in range(n) :
            visited[i][j] = 0

print(ret)
