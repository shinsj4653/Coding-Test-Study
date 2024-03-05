# 최대한 몇 칸 지날 수 있는지
# 이건 bfs가 가능한가??
# 어느 방향으로 가는지에 따라 최대 길이가 달라짐

# dfs
# 지금까지의 경로 배열 상태값으로 두면서
# 그리고 끝나면 원복
# 경로 배열 말고 차라리 A 부터 Z 배열?
# -> 이게 방문 여부 체크하는게 더 수월할수도?

# 알파벳 방문 -> = 1 이 아니라 += 1로 해야됨
# 원복할 때도 = 0 이 아니라 -= 1로
# 그래야 C A A 에서 원복 할때 C A -> A가 0이 되면 방문안할걸로 처리되기 때문

# 반례까지 완료하니 정답!!

from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

visited = [[0 for _ in range(c)] for _ in range(r)]
alpha = [0 for _ in range(26)] # 0부터 25 -> 총 26개 알파벳
 # 시작지점 알파벳 방문 체크
visited[0][0] = 1
ret = 1

# visited[0][0] = 1
# alpha[ord(board[0][0]) - ord('A')] += 1

def dfs(y, x, way) :

    global ret
    # way.append(board[y][x])

    if alpha[ord(board[y][x]) - ord('A')] > 0 :
        ret = max(ret, way - 1)
        return

    visited[y][x] = 1
    alpha[ord(board[y][x]) - ord('A')] += 1

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] :
            dfs(ny, nx, way + 1)
            # 원복

    ret = max(ret, way) # 기저사례에 안걸리지만, way 값 업데이트 해줘야 하는 경우
    # 2 1
    # A
    # C
    # 혹은
    # 1 2
    # AC - 기저사례에 안 걸림 -> 그래서 원복 전에 way값으로 ret 업데이트 필요함
    visited[y][x] = 0
    alpha[ord(board[y][x]) - ord('A')] -= 1
    return


dfs(0, 0, 1)
print(ret)