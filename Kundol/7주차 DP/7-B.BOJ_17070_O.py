# 1 1 0 0
# 0 0 1 0
# 0 0 1 0
# 0 0 0 1

# 1 1 1 0
# 0 0 0 1
# 0 0 0 1
# 0 0 0 1

# 1 1 0 0
# 0 0 1 0
# 0 0 0 1
# 0 0 0 1
import sys

input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(form, ey, ex) :
    global answer

    if ey == n - 1 and ex == n - 1 :
        answer += 1
        return

    if form == 0 : #가로
        # 가로 -> 가로
        if ex + 1 < n and house[ey][ex + 1] != 1 :
            dfs(0, ey, ex + 1)

        # 가로 -> 대각선
        if ey + 1 < n and ex + 1 < n \
            and house[ey][ex + 1] != 1 and house[ey + 1][ex] != 1 and house[ey + 1][ex + 1] != 1 :
            dfs(2, ey + 1, ex + 1)

    elif form == 1 : #세로
        # 세로 -> 세로
        if ey + 1 < n and house[ey + 1][ex] != 1:
            dfs(1, ey + 1, ex)

        # 세로 -> 대각선
        if ey + 1 < n and ex + 1 < n \
                and house[ey][ex + 1] != 1 and house[ey + 1][ex] != 1 and house[ey + 1][ex + 1] != 1:
            dfs(2, ey + 1, ex + 1)

    else : #대각선
        # 대각선 -> 가로
        if ex + 1 < n and house[ey][ex + 1] != 1:
            dfs(0, ey, ex + 1)

        # 대각선 -> 세로
        if ey + 1 < n and house[ey + 1][ex] != 1:
            dfs(1, ey + 1, ex)

        # 대각선 -> 대각선
        if ey + 1 < n and ex + 1 < n \
                and house[ey][ex + 1] != 1 and house[ey + 1][ex] != 1 and house[ey + 1][ex + 1] != 1:
            dfs(2, ey + 1, ex + 1)


dfs(0, 0, 1) # form : 0 == 가로, 1 : 세로, 2 : 대각선
print(answer)