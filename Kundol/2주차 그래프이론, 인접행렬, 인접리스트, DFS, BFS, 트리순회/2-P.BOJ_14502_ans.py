# 맞왜틀
# -> 해결!
# 벽 세우는 것 뿐만 아니라, 바이러스 퍼뜨린 것도 초기화 해줘야함!

# 정답
# 3단계 로직 존재
# 1. 벽 세우기
# 2. 바이러스 퍼지기
# 3. 퍼지고 나서 안전 영역 카운트해서 max 시키기

# 벽을 어떻게 효율적으로 세울까? 라고 생각부터 하는 것이 아니라,
# 무식하게 벽을 세운다는 생각을 먼저 해야한다!
# -> 모든 경우의 수를 구하는 것을 고려해보고, 그 다음에! 효율적으로 하는 것을 생각!
# 문제의 최대범위 기반으로 시간복잡도 유추하기

# 맵의 최대범위: 8 * 8 -> 64
# 벽의 순서는 상관 없다 -> 조합
# 64C3 * (64 + 64)
# 벽고르고 * (바이러스 dfs 탐색 + 0인 영역 카운트)

from itertools import combinations

from itertools import combinations

n, m = map(int, input().split()) # 세로 n, 가로 m
lab = []

walls = []
virus = []
ret = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, v) :
    v[y][x] = 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m :
            if lab[ny][nx] == 0 and not visited[ny][nx]:
                dfs(ny, nx, v)

    return

for i in range(n) :
    l = list(map(int, input().split()))
    for j in range(m) :
        if l[j] == 0 :
            walls.append((i, j))
    lab.append(l)

for c in combinations(walls, 3) :

    # 벽 세우기
    lab[c[0][0]][c[0][1]] = 1
    lab[c[1][0]][c[1][1]] = 1
    lab[c[2][0]][c[2][1]] = 1

    # 방문 배열 초기화
    visited = [[0 for _ in range(m)] for _ in range(n)]

    # dfs 실행
    # 2인 요소 찾으면 그 위치를 기준으로 dfs
    # 상하좌우로 2 물들이고, 다 하고나면 0 개수 구하기
    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 2 and not visited[i][j]:
                dfs(i, j, visited)

    zcnt = 0

    # lab 이 0인데, 방문하지 않았다면, 바이러스가 퍼지지 않았다는 소리!
    # 이런로직이면 lab_copy 필요 없다


    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 0 and not visited[i][j] :
                zcnt += 1

    ret = max(ret, zcnt)

    # 다시 원상복구
    # 벽 세운거 원상복구
    lab[c[0][0]][c[0][1]] = 0
    lab[c[1][0]][c[1][1]] = 0
    lab[c[2][0]][c[2][1]] = 0

print(ret)
