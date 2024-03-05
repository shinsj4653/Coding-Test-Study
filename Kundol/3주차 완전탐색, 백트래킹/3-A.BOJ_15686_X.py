# M -> 유지할 치킨집 개수
# 우선 치킨집의 좌표 리스트 뽑기
# -> 이 중 M개 고른다음,
# 거리 계산 후, 가장 min 값 구하기
# -> 각 2당 거리 계산 하고 나면 거리 배열 초기화
# 각 M개 고를 때마다 visited 배열 초기화

# 그리고 문제를 잘 읽자..
# 치킨 거리 -> 모든 치킨집에서의 집 까지의 거리의 합이 아니라,
# 모든 집에서 치킨집까지의 거리의 합

# 최단거리 -> DFS가 아닌 BFS로!!

from itertools import combinations
from collections import deque

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
chicken = []
q = deque()

ret = 1e9

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 2 :
            chicken.append((i, j))

def dfs(y, x, way, ways) :

    print(f"arrived at {y}, {x}")
    visited[y][x] = 1
    print('current way value : ', way)

    if city[y][x] == 3 : # 살아있는 치킨집일 경우
        print('find chicken : ', way)
        ways.append(way)
        return

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n :
            if not visited[ny][nx] :
                print('dfs start')
                dfs(ny, nx, way + 1, ways)
                print('dfs end')

def bfs(v, ways) :
    while q :
        y, x = q.popleft()
        v[y][x] = 1

        if city[y][x] == 3 :
            print('find chicken!')
            print(f'append {y},{x}')
            print(f'way value : {v[y][x] - 1}')
            ways.append(v[y][x] - 1)

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n :
                if not v[ny][nx] :
                    v[ny][nx] = v[y][x] + 1
                    q.append((ny, nx))

for c in combinations(chicken, m) :

    ways = []
    for y, x in c: # 치킨집 중 최대 M개 골라서 살리기
        print('select alive chicken : ', y, ",", x)
        city[y][x] = 3

    print(city)

    for i in range(n) :
        for j in range(n) :
            if city[i][j] == 1 :
                print('find chicken start : ', i, ',', j)
                q = deque()
                q.append((i, j))
                visited = [[0 for _ in range(n)] for _ in range(n)]  # visited 초기화
                print('bfs start')
                bfs(visited, ways)
                print('bfs end')

    ways.sort() # 오름차순 정렬
    print(ways)
    #ret = min(ret, sum(ways[:]))
    # 다시 복원
    for y, x in c:
        city[y][x] = 2

#print(ret)