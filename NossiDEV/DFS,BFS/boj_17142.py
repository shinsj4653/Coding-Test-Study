from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 10 ** 6

# 바이러스로 방 꽉 찼는지 체크
def isFullWithVirus(lab) :
    for y in range(n) :
        for x in range(n) :
            if lab[y][x] == -1 :
                return False

    return True

def bfs(v) :

    global answer
    q = deque()

    for r, c in v :
        q.append([r, c, 0])

    temp = [lab[i][:] for i in range(n)]

    max_time = 0

    while q :
        cy, cx, ctime = q.popleft()

        for i in range(4) :
            ny = cy + dy[i]
            nx = cx + dx[i]
            ntime = ctime + 1

            if 0 <= ny < n and 0 <= nx < n :
                if temp[ny][nx] == -1 :
                    temp[ny][nx] = ntime
                    max_time = max(max_time, ntime)
                    q.append([ny, nx, ntime])
                elif temp[ny][nx] == '*' : # 굳이 출발지점으로 넣을 필요는 없다!!
                    # 그저 바이러스가 전염될 수 있다는 거다
                    # 만약 '*' 칸이 맨 구석 끝에 있다면, time이 1초 더 늘어남
                    # 문제 예시에서 볼 수 있듯이, 다음 지점으로 포함은 시키되, 시간 갱신을 할 필요는 없다
                    temp[ny][nx] = ntime
                    q.append([ny, nx, ntime])

    if isFullWithVirus(temp) :
        answer = min(answer, max_time)

    return

virus = []

for y in range(n) :
    for x in range(n) :
        if lab[y][x] == 0 :
            lab[y][x] = -1

        elif lab[y][x] == 1 :
            lab[y][x] = '-'

        elif lab[y][x] == 2 :
            virus.append([y, x])
            lab[y][x] = '*'

for c in combinations(virus, m) :
    for y, x in c :
        lab[y][x] = 0

    bfs(c)

    for y, x in c :
        lab[y][x] = '*'


if answer == 10 ** 6 :
    answer = -1
print(answer)