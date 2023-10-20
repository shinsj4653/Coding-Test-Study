import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().rstrip().split())

maze = []

# J 좌표리스트
j_pos = deque([])

# F 좌표리스트
f_pos = deque([])


for i in range(r) :
    row = input().rstrip()
    line = []
    for j in range(len(row)) :
        line.append(row[j])

        if row[j] == 'J' :
            j_pos.append((i, j))

        if row[j] == 'F' :
            f_pos.append((i, j))

    maze.append(line)

for i in range(r) :
    for j in range(c) :
        if maze[i][j] == 'J' :
            maze[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :

    f_alt = deque()
    j_alt = deque()

    while True :

        # 불에 대한 BFS 먼저
        while f_pos :
            f_alt.append(f_pos.popleft())

        while f_alt :
            x, y = f_alt.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c :
                if maze[nx][ny] == '.' :
                    maze[nx][ny] = 'F'
                    f_pos.append((nx, ny))

        # j 이동
        # 만약, 이동시킬 좌표 없다면?? -> 탈출 불가능
        if len(j_pos) == 0 :
            print('IMPOSSIBLE')
            exit()

        while j_pos :
            j_alt.append(j_pos.popleft())

        while j_alt :
            x, y = j_alt.popleft()

            # 가장자리면 탈출!
            if x == 0 or x == r - 1 or y == 0 or y == c - 1 :
                print(maze[x][y])
                exit()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if maze[nx][ny] == '.':
                        maze[nx][ny] = maze[x][y] + 1
                        j_pos.append((nx, ny))

bfs()
