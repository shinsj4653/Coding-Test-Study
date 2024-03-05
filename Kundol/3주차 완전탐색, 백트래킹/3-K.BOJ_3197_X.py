# 우선 처음에 L과 L끼리 만날 수 있는 지 체크
# 모든 정점 탐색
# -> 만약 점이면 4방향 탐색
# -> X면 .으로 바꾸기

# 시간 초과 발생
# 3-J 문제랑 굉장히 유사한듯
# 2개의 큐와 2개의 temp를 써서 풀어보려 했지만
# 진정한 맞왜틀...


from collections import deque
import sys

input = sys.stdin.readline

# 2250000 200백만

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().rstrip().split())
lake = [list(input().rstrip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
day = 0

if r == 1 and c == 1 :
    print(0)
else :
    l1_y, l1_x, l2_y, l2_x = 0, 0, 0, 0
    found = False
    for i in range(r) :
        for j in range(c) :
            if lake[i][j] == 'L' and not found :
                l1_y, l1_x = i, j
                found = True
                continue
            elif lake[i][j] == 'L' and found :
                l2_y, l2_x = i, j
                break

    q = deque()
    q2 = deque([(l1_y, l1_x)])  # L 전용 bfs 큐

    lake[l1_y][l1_x] = '.'

    # 첫번째 때 출발점들 넣어줘야함
    for i in range(r) :
        for j in range(c) :
            if lake[i][j] == '.' :
                q.append((i, j))

            # 탐색해야 할 queue 다 찾았다면!
    while visited[l2_y][l2_x] != 2 :
        day += 1
        temp = deque()
        temp2 = deque()

        while q :
            y, x = q.popleft()

            for i in range(4) :
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] :
                    visited[ny][nx] = 1
                    if lake[ny][nx] == 'X':
                        lake[ny][nx] = '.'
                        temp.append((ny, nx))

                    elif lake[ny][nx] == '.':
                        q.append((ny, nx))
        q = temp

        while q2 :
            y, x = q2.popleft()
            visited[y][x] = 2

            for i in range(4) :
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] != 2 :
                    visited[ny][nx] = 2
                    if lake[ny][nx] == '.':
                        q2.append((ny, nx))

                    else :
                        temp2.append((ny, nx))

        if visited[l2_y][l2_x] == 2 :
            break

        q2 = temp2

    print(day)
