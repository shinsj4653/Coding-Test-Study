# 맞긴했지만, 정석 풀이를 봐보자
n = int(input())
dp = [[[0 for _ in range(3)] for _ in range(n + 5)] for _ in range(n + 5)] # 0 : 가로, 1: 세로, 2 : 대각선

dp[1][2][0] = 1

h = [[0 for _ in range(n + 5)] for _ in range(n + 5)]

for i in range(1, n + 1) :
    li = list(map(int, input().split()))

    for j in range(1, n + 1) :
        h[i][j] = li[j - 1]

def check(y, x, d) :
    if d == 0 or d == 1 :
        if not h[y][x] : return True

    else :
        if h[y - 1][x] == 0 and h[y][x - 1] == 0 and h[y][x] == 0 :
            return True

    return False


for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if check(i, j + 1, 0) : dp[i][j + 1][0] += dp[i][j][0]
        if check(i + 1, j + 1, 2) : dp[i + 1][j + 1][2] += dp[i][j][0]

        if check(i + 1, j, 1) : dp[i + 1][j][1] += dp[i][j][1]
        if check(i + 1, j + 1, 2) : dp[i + 1][j + 1][2] += dp[i][j][1]

        if check(i, j + 1, 0) : dp[i][j + 1][0] += dp[i][j][2]
        if check(i + 1, j, 1) : dp[i + 1][j][1] += dp[i][j][2]
        if check(i + 1, j + 1, 2) : dp[i + 1][j + 1][2] += dp[i][j][2]

ret = dp[n][n][0] + dp[n][n][1] + dp[n][n][2]
print(ret)