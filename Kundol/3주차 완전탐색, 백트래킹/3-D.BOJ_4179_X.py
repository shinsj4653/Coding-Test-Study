# 가장 빠른 탈출시간 : 최단거리 -> BFS
# J와 F의 동시 bfs
# F를 bfs먼저 한 턴 돌리고, 그다음 J이동
# 탐색 끝나면, J가 가장 자리에 있는지 확인

# 우선 F 좌표 모두 추출
# -> 각 좌표 모두 순회하며 bfs
# 불은 동시에 퍼지기 때문

from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
fire = deque()

visited = [[0 for _ in range(c)] for _ in range(r)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(r) :
    for j in range(c) :
        if maze[i][j] == 'J' :
            visited[i][j] = 1

if r == 1 and c == 1 :
    print(1)

else :
    time = 1

    while True:
        ji = deque()
        flag = False
        escape = False

        for i in range(r):
            for j in range(c):
                if maze[i][j] == 'F':
                    fire.append((i, j))

        for i in range(r) :
            for j in range(c) :
                if visited[i][j] == 1 :
                    ji.append((i, j))

        while fire :
            y, x = fire.popleft()
            for i in range(4) :
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if maze[ny][nx] != '#' :
                        maze[ny][nx] = 'F' # 불 번지기

        while ji :
            jy, jx = ji.popleft()
            for i in range(4) :
                ny = jy + dy[i]
                nx = jx + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if maze[ny][nx] != '#' and maze[ny][nx] != 'F' :
                        visited[ny][nx] = 1
                        flag = True
                        if ny == 0 or ny == r - 1 or nx == 0 or nx == c - 1 :
                            escape = True
                            break
            if escape :
                break

        if escape:
            print(time + 1)
            break

        if not flag: # J가 이동 못했다면
            print('IMPOSSIBLE')
            break

        time += 1






# 가장 빠른 탈출시간 : 최단거리 -> BFS
# J와 F의 동시 bfs
# F를 bfs먼저 한 턴 돌리고, 그다음 J이동
# 탐색 끝나면, J가 가장 자리에 있는지 확인

# 우선 F 좌표 모두 추출
# -> 각 좌표 모두 순회하며 bfs
# 불은 동시에 퍼지기 때문

from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
fire = deque()

visited = [[0 for _ in range(c)] for _ in range(r)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(r) :
    for j in range(c) :
        if maze[i][j] == 'J' :
            visited[i][j] = 1

if r == 1 and c == 1 :
    print(1)

else :
    time = 1

    while True:
        ji = deque()
        flag = False
        escape = False

        for i in range(r):
            for j in range(c):
                if maze[i][j] == 'F':
                    fire.append((i, j))

        for i in range(r) :
            for j in range(c) :
                if visited[i][j] == 1 :
                    ji.append((i, j))

        while fire :
            y, x = fire.popleft()
            for i in range(4) :
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if maze[ny][nx] != '#' :
                        maze[ny][nx] = 'F' # 불 번지기

        while ji :
            jy, jx = ji.popleft()
            for i in range(4) :
                ny = jy + dy[i]
                nx = jx + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if maze[ny][nx] != '#' and maze[ny][nx] != 'F' :
                        visited[ny][nx] = 1
                        flag = True
                        if ny == 0 or ny == r - 1 or nx == 0 or nx == c - 1 :
                            escape = True
                            break
            if escape :
                break

        if escape:
            print(time + 1)
            break

        if not flag: # J가 이동 못했다면
            print('IMPOSSIBLE')
            break

        time += 1






