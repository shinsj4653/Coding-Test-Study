# 정답
# 2가지 로직 필요
# 1. 백조가 움직이는 moveSwan이 필요
# 2. 얼음이 하루마다 녹는 로직 필요 watermelt

# 문제를 단순화 시켜보자
# 백조 하나를 기반으로 floodfill -> queue를 2개를 써서

# 아이디어는 맞았지만 구현하는 방법을 다시 꼼꼼히 복습해보기

# https://dev-code-notepad.tistory.com/97
# -> 덱 복사하는 방법 공부!

from collections import deque

# 2250000 200백만

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
swanY, swanX = 0, 0
waterQ = deque()
swanQ = deque()
swan_tempQ = deque()
water_tempQ = deque()

r, c = map(int, input().split())

visited = [[0 for _ in range(c)] for _ in range(r)]
visited_swan = [[0 for _ in range(c)] for _ in range(r)]
lake = []
day = 0

def water_melting() :
    while waterQ :
        y, x = waterQ.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] :
                if lake[ny][nx] == 'X' :
                    visited[ny][nx] = 1
                    water_tempQ.append((ny, nx))
                    lake[ny][nx] = '.'


def move_swan() :
    while swanQ :
        y, x = swanQ.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c and not visited_swan[ny][nx] :
                visited_swan[ny][nx] = 1
                if lake[ny][nx] == '.' :
                    swanQ.append((ny, nx))

                elif lake[ny][nx] == 'X' :
                    swan_tempQ.append((ny, nx))

                elif lake[ny][nx] == 'L':
                    return True

    return False

for i in range(r) :
    row = list(input())
    for j in range(c) :
        if row[j] == 'L' :
            swanY = i
            swanX = j
        if row[j] == '.' or row[j] == 'L' :
            visited[i][j] = 1
            waterQ.append((i, j))
    lake.append(row)

swanQ.append((swanY, swanX))
visited_swan[swanY][swanX] = 1

while True :
    if move_swan() :
        break
    water_melting()
    waterQ = water_tempQ.copy()
    swanQ = swan_tempQ.copy()
    water_tempQ.clear()
    swan_tempQ.clear()
    day += 1

print(day)