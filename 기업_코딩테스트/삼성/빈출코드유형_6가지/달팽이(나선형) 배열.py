# 안에서 밖으로

arr = [[0] * 5 for _ in range(5)]

def tornado():
    global arr
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y = len(arr) // 2
    x = len(arr) // 2
    num = 0  # 칸에 채워넣을 값
    dist = 1
    d_idx = 0  # 서 남 동 북 순서
    move_count = 0  # 2가 되면 dist 길이가 1 늘어나고 move_count는 다시 0으로 초기화
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = dy + y
            X = dx + x
            if (Y, X) == (0, -1):  # 0행 -1열이 토네이도가 모두 끝나고 나서의 위치임
                return
            num += 1
            arr[Y][X] = num
            y = Y
            x = X
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0

tornado()

# 밖에서 안으로
def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0 for j in range(n)] for i in range(n)]  # 배열 초기화

    x = 0
    y = 0
    d_idx=0

    for i in range(n * n):
        answer[x][y] = i + 1
        if d_idx == 0:
            y += 1
            if y == n - 1 or answer[x][y + 1] != 0:  # 맨 끝에 도달했거나 가려는 곳에 이미 값이 있으면 방향 전환
                d_idx = 1
        elif d_idx == 1:
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0:
                d_idx = 2
        elif d_idx == 2:
            y -= 1
            if y == 0 or answer[x][y - 1] != 0:
                d_idx = 3
        elif d_idx == 3:
            x -= 1
            if x == n - 1 or answer[x - 1][y] != 0:
                d_idx = 0

    return answer


arr=solution(5)
for i in range(len(arr)):
    print(arr[i])