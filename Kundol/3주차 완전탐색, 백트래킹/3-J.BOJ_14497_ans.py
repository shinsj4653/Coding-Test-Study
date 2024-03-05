# 정답
# 만약 2차원 이해 안되면 1차원으로 생각해보기
# 0 -> 계속 탐색
# 1 -> 멈춰서 cnt 업

# bfs에서 큐를 2개 사용하는 방법도 존재

from collections import deque

n, m = map(int, input().split())
ret = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y1, x1, y2, x2 = map(int, input().split())
room = [list(input()) for _ in range(n)]

visited = [[0 for _ in range(301)] for _ in range(301)]
y1 -= 1
x1 -= 1
y2 -= 1
x2 -= 1

q = deque([1000 * y1 + x1]) # 최대 범위가 300이기 때문
cnt = 0

while room[y2][x2] != '0' :
    cnt += 1
    temp = deque()

    while q :
        num = q.popleft()
        y = num // 1000
        x = num % 1000

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] :
                visited[ny][nx] = cnt

                if room[ny][nx] != '0' :
                    room[ny][nx] = '0'
                    temp.append(1000 * ny + nx) # 1은 레벨 늘리고 temp에 넣기
                    # 즉, temp는 다음에 탐색할 정점들
                else :
                    q.append(1000 * ny + nx) # 0은 계속 탐색

    q = temp

print(visited[y2][x2])