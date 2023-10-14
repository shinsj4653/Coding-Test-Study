n, m = map(int, input().split())
square = []
answer = 1

for i in range(n):
    row = list(map(int, list(input())))
    square.append(row)

# 가장 큰 정사각형
# 가로, 세로 same

# 완탐
num = min(n, m)
for len in range(1, num) :
    for x in range(n) :
        for y in range(m) :
            if x + len > n - 1 or y + len > m - 1 :
                break

            if square[x][y] == square[x + len][y] \
                == square[x][y + len] == square[x + len][y + len] :
                answer = (len + 1) * (len + 1)

print(answer)
