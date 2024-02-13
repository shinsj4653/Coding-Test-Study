# 안전 영역의 최대 크기
# 8 * 8 * 62 -> 빈칸 모두 일일이 다 해봐도 괜춘!
# 무식하게!

from itertools import combinations

n, m = map(int, input().split()) # 세로 n, 가로 m
lab = []

zeros = []
ret = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, v, lab_copy) :
    v[y][x] = 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m :
            if lab_copy[ny][nx] == 0 and not visited[ny][nx]:
                lab_copy[ny][nx] = 2 # 바이러스 전파
                dfs(ny, nx, v, lab_copy)

    return

for i in range(n) :
    l = list(map(int, input().split()))
    for j in range(m) :
        if l[j] == 0 :
            zeros.append((i, j))
    lab.append(l)

for c in combinations(zeros, 3) :
    # 매 턴 마다 연구실 원본 가져와야함
    lab_copy = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n) :
        for j in range(m) :
            lab_copy[i][j] = lab[i][j]

    # 벽 세우기
    lab_copy[c[0][0]][c[0][1]] = 1
    lab_copy[c[1][0]][c[1][1]] = 1
    lab_copy[c[2][0]][c[2][1]] = 1

    # 방문 배열 초기화
    visited = [[0 for _ in range(m)] for _ in range(n)]

    # dfs 실행
    # 2인 요소 찾으면 그 위치를 기준으로 dfs
    # 상하좌우로 2 물들이고, 다 하고나면 0 개수 구하기
    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 2 and not visited[i][j]:
                dfs(i, j, visited, lab_copy)

    zcnt = 0
    #  0개수 count
    #print(lab)
    for i in range(n) :
        for j in range(m) :
            if lab_copy[i][j] == 0 :
                zcnt += 1

    ret = max(ret, zcnt)

    # 다시 원상복구
    # 벽세운거 말고도, 바이러스 퍼뜨린것도 원상복구 해야됨!

print(ret)