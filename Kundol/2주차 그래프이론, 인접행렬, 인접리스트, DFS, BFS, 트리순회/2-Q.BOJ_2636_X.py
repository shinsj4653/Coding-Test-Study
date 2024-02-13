# 치즈 중 가장 겉 부분을 어떻게 판단??

# 예시 그림 처럼 'c'를 마킹해야함!
# -> 그래야 맨 끝의 'c'를 기준으로 bfs 할 수 있음
# -> 가운데 구멍인지는 어떻게 알지?

# 정답
# 문제에선 녹인다, 삭제한다
# -> 구현으로는 칠하기, 변경하기로 풀기 가능

# 핵심 로직
# -> 끝부분에는 치즈가 없다!
# -> 그 말은, 끝부분 0,0 에서 시작하고 1 발견하는 순간 dfs 멈추면,
# 가장 끝 치즈를 구할 수 있다!!!!
import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split()) #세로n 가로m
a = [list(map(int, input().split())) for _ in range(n)]
visited = []
v = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0

def go(y, x) :
    visited[y][x] = 1
    if a[y][x] == 1 :
        v.append((y, x))
        return

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m :
            if not visited[ny][nx] :
                go(ny, nx)

    return

while True :
    visited = [[0 for _ in range(m)] for _ in range(n)]
    v = [] # 치즈 녹아야하는 부분
    go(0, 0)

    cnt2 = len(v) # 녹기 전 사이즈

    for b in v :
        a[b[0]][b[1]] = 0

    flag = 0
    for i in range(n) :
        for j in range(m) :
            if a[i][j] != 0:
                flag = 1

    cnt += 1
    if not flag : # 치즈 다 사라졌으면 break
        break

print(cnt)
print(cnt2)

