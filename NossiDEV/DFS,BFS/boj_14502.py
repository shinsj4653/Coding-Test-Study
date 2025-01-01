from itertools import combinations
from collections import deque, Counter

n, m = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

def bfs(y, x, v) :
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.popleft()

        for i in range(4) :
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < m and v[ny][nx] == 0 :
                v[ny][nx] = 2
                q.append((ny, nx))

# 0인 지점 저장
pillars = []
for y in range(n) :
    for x in range(m) :
        if map_data[y][x] == 0 :
            pillars.append((y, x))

for c in combinations(pillars, 3) :
    # 원본 map 복사
    v = [[0 for _ in range(m)] for _ in range(n)]

    for y in range(n) :
        for x in range(m) :
            v[y][x] = map_data[y][x]

    # 기둥 세우기
    v[c[0][0]][c[0][1]] = 1
    v[c[1][0]][c[1][1]] = 1
    v[c[2][0]][c[2][1]] = 1

    for y in range(n) :
        for x in range(m) :
            if v[y][x] == 2 :
                bfs(y, x, v)

    safe_area = 0
    for row in v :
        safe_area += (Counter(row)[0])

    answer = max(answer, safe_area)

print(answer)