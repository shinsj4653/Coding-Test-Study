# 정답
# 문제를 보시고, 시간복잡도 항상 먼저 계산해봐야한다!
# 이 문제는 -> 완탐이 아닌 백트래킹
# 사다리 점점 증가시키는데, 최솟값을 구하므로,
# -> 최솟값보다 더 큰 값이 되어버리면 해당 경로는 가지 않기

# visited[a][b] -> 1(높이) 1(세로선) 위치에 사다리를 둔다!

from collections import defaultdict
INF = 10e9

n, m, h = map(int, input().split())

visited = [[0 for _ in range(34)] for _ in range(34)]

for i in range(m) :
    a, b = map(int, input().split())
    visited[a][b] = 1

ret = INF

# check -> i번 사다리가 i번에 도착하는지 체크
def check() :
    for i in range(1, n + 1) :
        start = i
        for j in range(1, h + 1) :
            if visited[j][start] : start += 1
            elif visited[j][start - 1] : start -= 1

        if start != i : return False

    return True

def go(here, cnt) :
    global ret
    if cnt > 3 or cnt >= ret : return
    if check() :
        ret = min(ret, cnt)

    for i in range(here, h + 1) :
        for j in range(1, n + 1) :
            if visited[i][j] or visited[i][j - 1] or visited[i][j + 1] : continue
            visited[i][j] = 1
            go(i, cnt + 1)
            visited[i][j] = 0


go(1, 0)
print(-1) if ret == INF else print(ret)