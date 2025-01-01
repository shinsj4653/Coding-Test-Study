# print(16*16*16)

from collections import deque

answer = 16 * (10 ** 6) + 2

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n)] # i 에서 출발했을 때의 최소 전체 순환 거리

track = deque()

# 4 -> 3
# 3 -> 1
# 1 -> 2
# 2 -> 4

def dfs(start_i, track) :

    global answer

    if len(track) == n :
        if track[0][0] == track[n - 1][1] :
            if dp[track[0][0]] == 0 :
                fr = [0 for _ in range(n)]
                to = [0 for _ in range(n)]
                num = 0
                for t in track :
                    fr[t[0]] += 1
                    to[t[1]] += 1

                    if fr[t[0]] > 1 or to[t[1]] > 1 :
                        return

                    num += t[2]

                dp[track[0][0]] = num

            answer = min(answer, dp[track[0][0]])
        return

    for j in range(n) :
        if w[start_i][j] != 0 :
            track.append((start_i, j, w[start_i][j]))
            tmp = w[start_i][j]
            w[start_i][j] = 0

            dfs(j, track)

            w[start_i][j] = tmp
            track.pop()

for i in range(n) :
    dfs(i, track)

print(answer)