# 정답
# alpha 배열 하나로도 가능!

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


# visited[0][0] = 1
alpha[ord(board[0][0]) - ord('A')] = 1

def dfs(y, x, way) :

    global ret
    ret = max(ret, way) # 계속 max 업데이트
    # 그래야 1 2, 2 1짜리 반례도 반영 가능
    # alpha 값이 1보다 큰 경우만 기저사례로 치면 안됨

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c :

            next = ord(board[ny][nx]) - ord('A')

            if alpha[next] == 0:
                alpha[next] = 1
                dfs(ny, nx, way + 1)
                alpha[next] = 0
    return


dfs(0, 0, 1)
print(ret)