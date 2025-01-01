# xxx
# oo.
# xxx

# OOXXXOOXO
# oox
# xxo
# oxo

# x, O의 가로, 세로, 대각선 줄 갯수
# x, o의 개수 기록

li = []

while(True) :

    line = input()

    if line == 'end' :
        break

    li.append(list(line))

t_li = []

for l in li :
    t = [[' ' for _ in range(3)] for _ in range(3)]

    for i in range(3) :
        for j in range(3) :
            t[i][j] = l[i * 3 + j]

    t_li.append(t)

for tic in t_li :
    # 틱택토 2차원 배열
    #print(tic)
    x_cnt, o_cnt = 0, 0 # 무조건 x 먼저이니 x의 개수가 더 많아야함
    x_t_cnt, o_t_cnt = 0, 0 # 한줄 완성한 갯수 -> 총 8의 경우의 수

    for i in range(3) :
        for j in range(3) :
            if tic[i][j] == 'X' :
                x_cnt += 1

            elif tic[i][j] == 'O' :
                o_cnt += 1


        if tic[0][j] == 'X' and tic[0][j] == tic[1][j] and tic[1][j] == tic[2][j] :
            x_t_cnt += 1

        elif tic[0][j] == 'O' and tic[0][j] == tic[1][j] and tic[1][j] == tic[2][j] :
            o_t_cnt += 1

        if tic[i][0] == 'X' and tic[i][0] == tic[i][1] and tic[i][1] == tic[i][2] :
            x_t_cnt += 1

        elif tic[i][0] == 'O' and tic[i][0] == tic[i][1] and tic[i][1] == tic[i][2] :
            o_t_cnt += 1

    # 대각선
    if tic[0][0] == 'X' and tic[0][0] == tic[1][1] and tic[1][1] == tic[2][2] :
        x_t_cnt += 1

    elif tic[0][0] == 'O' and tic[0][0] == tic[1][1] and tic[1][1] == tic[2][2] :
        o_t_cnt += 1

    if tic[0][2] == 'X' and tic[0][2] == tic[1][1] and tic[1][1] == tic[2][0] :
        x_t_cnt += 1

    elif tic[0][2] == 'O' and tic[0][2] == tic[1][1] and tic[1][1] == tic[2][0] :
        o_t_cnt += 1

    # print('x_cnt : ', x_cnt)
    # print('y_cnt : ', o_cnt)
    # print('x_t_cnt : ', x_t_cnt)
    # print('o_t_cnt : ', o_t_cnt)

    isValid = False

    if x_t_cnt > o_t_cnt : # X가 이긴 경우
        if x_cnt - o_cnt == 1 :
            isValid = True

    if x_t_cnt < o_t_cnt :
        if x_cnt == o_cnt :
            isValid = True

    if x_t_cnt == 0 and o_t_cnt == 0 :
        if x_cnt == 5 and o_cnt == 4 :
            isValid = True

    if x_t_cnt == 2 and x_cnt == 5 and o_cnt == 4 :
        isValid = True

    print('valid') if isValid else print('invalid')

    # xxo
    # oxx
    # xoo
