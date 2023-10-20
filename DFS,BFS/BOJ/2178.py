import sys
input = sys.stdin.readline

# 4, 6
n, m = map(int, input().split())

maze = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n) : # 0 ~ 3
    row = input()

    for j in range(m) : # 0 ~ 5
        maze[i + 1][j + 1] = int(row[j])

print(maze)

answer = 0
def bfs(x, y) :
    
