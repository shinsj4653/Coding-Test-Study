import collections

# sort 하는 방법 -> key 구문 까먹지 않도록 주의...

t = int(input())
for loop in range(t) :


    n, k, t, m = map(int, input().split())

    solve = []

    is_solved = [[0 for _ in range(k)] for _ in range(n)]
    score = [[0 for _ in range(k)] for _ in range(n)]
    time = [0 for _ in range(n)]

    time_num = 1

    for input_line in range(m) :
        i, j, s = map(int, input().split())
        i = i - 1
        j = j - 1
        solve.append((i, j ,s))

        if is_solved[i][j] == 0 :
            score[i][j] += s

        else :
            if s > score[i][j] :
                score[i][j] = s

        is_solved[i][j] += 1
        time[i] = time_num
        time_num += 1


    # 팀 번호, 최종 점수, 풀이 제출 횟수, 시간
    final = []

    for i in range(n) :
        final.append((i + 1, sum(score[i]), sum(is_solved[i]), time[i]))


    final.sort(key = lambda x : (-x[1], x[2], x[3]))
    # print(final)

    index = 0
    for f in final :
        if f[0] == t :
            print(index + 1)
        index += 1









