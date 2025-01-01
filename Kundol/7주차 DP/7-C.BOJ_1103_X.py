# 만약 다음 위치가 H 이거나,보트 벗어나는 자리면 가지 않음
# 아니라면 누적합으로 넘어가기
# 만약 누적합 수가 n * n 넘어가면 -1 반환
import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
boat = [list(input()) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

sy, sx = 0, 0
dp[sy][sx] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def check(y, x) :
    if 0 <= y < n and 0 <= x < m and boat[y][x] != 'H' :
        return True

    return False

answer = 1

isInfinite = False
def dfs(sy, sx) :
    global answer
    global isInfinite

    if dp[sy][sx] > n * m:
        isInfinite = True
        return

    if not check(sy, sx) :
        # 'H' 일 경우
        answer = max(answer, dp[sy][sx])
        return

    move = int(boat[sy][sx])

    for i in range(4) :
        ny = sy + dy[i] * move
        nx = sx + dx[i] * move

        if check(ny, nx) :
            dp[ny][nx] = dp[sy][sx] + 1
            num = dfs(ny, nx)
            if num : # None type 일수도 있기 때문
                answer = max(answer, num)
            dp[ny][nx] = dp[sy][sx] - 1

    return dp[sy][sx]

dfs(sy, sx)

if isInfinite:
    print(-1)

else :
    print(answer)