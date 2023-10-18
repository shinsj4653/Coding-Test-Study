# 사각 지대의 최소 크기
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board1 = []
board2 = []

for i in range(n) :
    board1.append(list(map(int, input().split())))

print(board1)

# 남, 동, 북, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 1번 : 4방향
# 2번 : 2방향
# 3번 : 4방향
# 4번 : 4방향
# 5번 : 1방향

# 백트래킹은 맞는 것 같긴한데..
# 카메라 당 방향이 너무 많은데..
# 진법 사용 -> 4진법!

def oob(a, b) :
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x, y, dir) :
    dir %= 4
    while True :




