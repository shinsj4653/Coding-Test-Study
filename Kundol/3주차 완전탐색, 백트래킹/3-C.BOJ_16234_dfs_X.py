# dfs
# 같은 영역 끼리 v배열에 넘버링
# -> 같은 영역이 되는 조건 -> 두 지점 수 차이가 l이상 r이하
# 같은 영역 탐색 끝나고, 같은 영역 내 숫자들 평균 값으로 업데이트
# -> v 배열 원소 모두 0이면 인구이동 없는 경우!


# 50 * 50 * 2000
# -> 2500000
# 2천만 -> 완탐하기 충분

# 의문점
# visited 배열이랑 area 배열이랑 따로 둬야해야하나?
# area만 있어도 될 것 같은데 실행이 안됨...

# dfs로 했을 때 메모리 초과나서 bfs로 바꿔보기로 함


import sys
sys.setrecursionlimit(10**9)

n, l, r = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
#area = [[0 for _ in range(n)] for _ in range(n)]
#v = [[0 for _ in range(n)] for _ in range(n)]
ret = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def isMove(area) :
    for i in range(n) :
        for j in range(n) :
            if area[i][j] :
                return True

    return False

def dfs(y, x, mark) :

    area[y][x] = mark

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n :
            if not area[ny][nx] and l <= abs(land[y][x] - land[ny][nx]) <= r :
                area[y][x] = mark
                area[ny][nx] = mark # 영역 색칠
                dfs(ny, nx, mark)

while True :
    mark = 1
    #v = [[0 for _ in range(n)] for _ in range(n)]
    area = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if not area[i][j] :
                dfs(i, j, mark)
                mark += 1
    #print(area)
    #print(land)
    # area 배열 모두 0
    # 즉 dfs 한번도 시행 x -> 인구이동 멈춤
    if not isMove(area):
        break

    #print('mark: ', mark)

    # 만약 칠 한 영역 있다면? 인구 이동 시작
    for num in range(1, mark) :
        li = []
        for i in range(n) :
            for j in range(n) :
                if area[i][j] == num :
                    li.append((i, j))

        sum_num = 0
        if len(li) > 0: # li가 없을 수도 있음
            for y, x in li :
                sum_num += land[y][x]

            avg_num = sum_num // len(li)
            for y, x in li :
                land[y][x] = avg_num

    ret += 1

print(ret)