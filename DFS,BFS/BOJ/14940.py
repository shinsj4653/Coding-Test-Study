import sys
input = sys.stdin.readline

n, m = int(input().split())

map = []
x, y = 0, 0

for i in range(n) :
    line = list(map(int, input().split()))
    map.append(line)

    # 2부터 시작 위치
    if line.find(2) != -1 :
        y = line.find(2)


