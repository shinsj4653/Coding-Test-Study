from collections import deque

n, m, r = map(int, input().split())

arr = []
new_arr = [[0 for _ in range(m)] for _ in range(n)]
q = deque()

for i in range(n) :
    arr.append(list(map(int, input().split())))

loops = min(n, m)

for i in range(loops) :
    q.clear()
    q.extend(arr[i][i:m - i]) # arr[0][0:4]
    q.extend([row[m - i - 1] for row in arr[i + 1:n - i - 1]])  #row[3] arr[1:3]
    q.extend(arr[n - i - 1][i:m - i][::-1])
    q.extend([row[i] for row in arr[i + 1:n - i - 1]][::-1])

    q.rotate(-r)

    for j in range(i, m - i):  # 상
        new_arr[i][j] = q.popleft()
    for j in range(i + 1, n - i - 1):  # 우
        new_arr[j][m - i - 1] = q.popleft()
    for j in range(m - i - 1, i - 1, -1):  # 하
        new_arr[n - i - 1][j] = q.popleft()
    for j in range(n - i - 2, i, -1):  # 좌
        new_arr[j][i] = q.popleft()

print(new_arr)