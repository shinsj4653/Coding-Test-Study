import sys
input = sys.stdin.readline

bingo = []

for i in range(5) :
    bingo.append(list(map(int, input().split())))

cnt = 1

def mark(n, cnt) :
    for i in range(5) :
        for j in range(5) :
            if bingo[i][j] == n :
                bingo[i][j] = 0

    b_cnt = 0

    if cnt >= 12 :
        # 이제 빙고 3개인지 검사 가능
        

for i in range(5) :
    nums = list(map(int, input().split()))
    for n in nums :
        n = int(n)
        mark(n, cnt)



