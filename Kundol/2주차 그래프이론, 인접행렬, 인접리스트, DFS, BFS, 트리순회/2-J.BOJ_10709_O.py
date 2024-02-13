# 거리 측정 -> BFS?
# BFS 말고 한줄마다 탐색
# c 있다면 flag = 1
# flag = 0일때는 -1, cloud 있을 때는 0하고 flag=1
# cloud 없지만 flag = 1이면 위치 차이값 넣기

h, w = map(int, input().split())
joi = [list(input()) for _ in range(h)]

for i in range(h) :
    flag = 0
    prev = 0
    for j in range(w) :
        if flag == 0 and joi[i][j] != 'c' :
            print(-1, end=" ")

        elif joi[i][j] == 'c' :
            print(0, end=" ")
            prev = j
            flag = 1

        elif flag == 1 and joi[i][j] != 'c' :
            print(j - prev, end=" ")

    print()
