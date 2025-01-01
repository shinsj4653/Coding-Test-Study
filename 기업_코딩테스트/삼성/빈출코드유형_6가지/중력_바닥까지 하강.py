arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

print("기존")
for i in range(len(arr)):
    print(arr[i])

def gravity():
    n = len(arr)
    m = len(arr[0])
    for i in range(n - 1):
        for j in range(m):
            p = i
            # 현재칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야함
            while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1


gravity()

print("변화")
for i in range(len(arr)):
    print(arr[i])