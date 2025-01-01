# 완탐 가능할듯?

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
answer = 64

for y in range(n - 8 + 1) :
    for x in range(m - 8 + 1) :
        # y, x : 체스판의 시작 위치
        chess = [[' ' for _ in range(8)] for _ in range(8)]

        for i in range(8) :
            for j in range(8) :
                chess[i][j] = board[y + i][x + j]

        for k in range(2) : # 'W' 시작 or 'B' 시작
            paint = 0
            if k == 0 :
                letter = 'W'

            else :
                letter = 'B'

            for i in range(8):
                for j in range(8):
                    if chess[i][j] != letter:
                        paint += 1

                    if j != 7 :
                        if letter == 'W' :
                            letter = 'B'
                        else :
                            letter = 'W'

            answer = min(answer, paint)


print(answer)