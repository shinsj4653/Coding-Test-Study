"""
1. 아이디어
- 2중 for문 => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 + 1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V + E)
- V = M * N = 500 * 500
- E = V * 4 = 500 * 500 * 4
- V + E : 5 * 250000 = 100만 < (1초에 2억 연산 가능) 2억 -> 가능!

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(bfs)
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
max_area = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x) :
    rs = 1
    q = deque([(y, x)])
    while q :
        ey, ex = q.popleft()
        for k in range(4) :
            # bfs 할 때, 4방향으로 탐색!

            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0 <= ny < n and 0 <= nx < m :
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))

    return rs

for j in range(n) :
    for i in range(m) :
        if map[j][i] == 1 and chk[j][i] == False :
            # 전체 그림 갯수를 + 1
            cnt += 1
            chk[j][i] = True
            # BFS를 통해 그림 크기를 구해주고
            max_area = max(max_area, bfs(j, i))
            # 최대값 갱신

print(cnt)
print(max_area)
