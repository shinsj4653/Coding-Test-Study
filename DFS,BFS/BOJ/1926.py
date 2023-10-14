# 이왜틀..

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n) :
    row = list(map(int, input().split()))
    graph.append(row)

q = deque(list())
cnt = 0
max_area = -1

for x in range(n) :
    for y in range(m) :

        if graph[x][y] == 1 :
            area = 0
            q.append((x, y))

            while q :
                x, y = q.popleft()
                graph[x][y] = 0
                area += 1

                if 0 <= x + 1 < n and 0 <= y + 1 < m :
                    if graph[x + 1][y] == 1 :
                        q.append((x + 1, y))

                    if graph[x][y + 1] == 1:
                        q.append((x, y + 1))

                    if graph[x - 1][y] == 1 :
                        q.append((x, y + 1))

                    if graph[x][y - 1] == 1 :
                        q.append((x, y - 1))

            max_area = max(max_area, area)
            cnt += 1
print(cnt)
print(max_area)
