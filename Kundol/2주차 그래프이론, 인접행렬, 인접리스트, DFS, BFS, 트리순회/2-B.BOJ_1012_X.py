# dfs - connected component
# 블로그 개념 보면서 복습하기
# RecursionError -> https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94
# 기본 재귀 깊이 제한을 풀어주자

import sys
sys.setrecursionlimit(10000)

t = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, g, visited, m, n) :

    visited[y][x] = 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m :
            continue

        if g[ny][nx] == 1 and visited[ny][nx] == 0 :
            dfs(ny, nx, g, visited, m, n)

    return

for _ in range(t) :
    ret = 0
    m, n, k = map(int, input().split())
    # m : 가로, n : 세로, k : 배추 위치 개수

    g = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for c in range(k) :
        x, y = map(int, input().split())
        g[y][x] = 1

    # dfs 시작
    for ay in range(n): # 세로
        for ax in range(m): # 가로
            if g[ay][ax] == 1 and visited[ay][ax] == 0 :
                dfs(ay, ax, g, visited, m, n)
                ret += 1

    print(ret)
