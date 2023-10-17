answer = 0
n = int(input())

# 퀸을 놓았는지, 그리고 어디에 놓았는지 판별하는 배열
is_used = [False] * n

# 체스판 현황
chess = [[0 for _ in range(n)] for _ in range(n)]

def modifyChess(x, y, num, chess) :
    # chess 판에서 x, y 기준으로 안되는 영역 모두 1로 두기
    for p in range(n):
        for q in range(n):
            if p == x or q == y:  # 기준 위치의 같은 가로, 세로에 모두 두면 x
                chess[p][q] = num

    # 대각선
    for r in range(1, n):
        if x - r >= 0 and y - r >= 0:
            chess[x - r][y - r] = num
        if x - r >= 0 and y + r < n:
            chess[x - r][y + r] = num
        if x + r < n and y - r >= 0:
            chess[x + r][y - r] = num
        if x + r < n and y + r < n:
            chess[x + r][y + r] = num

def func(x, y, chess) :
    global answer
    # 퀸을 모두 놓은 경우면, 경우의 수 +1 해줘야 함
    if is_used.count(False) == 0 :
        answer += 1
        return

    # 여기서 chess 판에서 퀸을 놓는 경우를 따져야 할듯
    # 즉, 다음 x,y를 판별해야 할듯??
    for i in range(n) :
        is_used[i] = True
        modifyChess(x, y, 1, chess)

        is_new_selected = False
        # 새로운 위치 선정
        for l in range(n) :
            for m in range(n) :
                if chess[l][m] == 0 :
                    is_new_selected = True
                    x = l
                    y = m
                    break

            if is_new_selected :
                break

        func(x, y, chess)

        is_used[i] = False
        # 마지막 요소 뽑고, 그 요소에 대해 판 원상 복귀
        # chess 판에서 x, y 기준으로 안되는 영역 모두 0로 두기
        modifyChess(x, y, 0, chess)

        # 단, 나머지 요소에 대해서는 아직 못 놓으므로 1 세팅 여전히 해둬야 함!
        for element in is_used :
            x, y = element
            modifyChess(x, y, 1, chess)


# 맨 첫 시작 위치 -> 0, 0
func(0, 0, chess)

if n == 1 :
    print(1)

elif n == 2 or n == 3 :
    print(0)

else :
    print(answer)

