# 최단거리 -> bfs
# 다음 탐색에 영향을 주면 안되니 원복해야함
# L과 L 사이의 최단거리중 가장 긴 값을 가지는 두 곳

# map의 모든 정점 for문
# 만약 l이면 bfs 실행
# -> 해당 map의 탐색 후, 가장 큰 번호 -> 최단 거리로 이동하는 시간
# 다시 map 초기화

# 정답
# visited 초기화하는 정석 방법
# -> bfs를 함수로 썼고, 함수 맨 위에 v배열 초기화 구문 넣어줌
# -> 나랑 똑같이 하셨다


from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

l, w = map(int, input().split())
v = [[0 for _ in range(w)] for _ in range(l)]
if l == 0 or w == 0 :
    print(0)

else :
    m = [list(input()) for _ in range(l)]
    ret = -100

    for i in range(l) :
        for j in range(w) :
            if m[i][j] == 'L':
                # visited 초기화
                v = [[0 for _ in range(w)] for _ in range(l)]
                v[i][j] = 1
                q = deque([(i, j)])

                while q :
                    y, x = q.popleft()

                    for k in range(4) :
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0 <= ny < l and 0 <= nx < w :
                            if not v[ny][nx] and m[ny][nx] == 'L' :
                                v[ny][nx] = v[y][x] + 1
                                q.append((ny, nx))

                # bfs 탐색이후
                for a in range(l) :
                    for b in range(w) :
                        ret = max(ret, v[a][b])


    print(ret - 1)