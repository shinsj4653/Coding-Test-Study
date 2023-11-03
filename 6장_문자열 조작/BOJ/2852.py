import sys

input = sys.stdin.readline

n = int(input())

t1_score = 0
t2_score = 0

t1_min, t1_sec = 0, 0
t2_min, t2_sec = 0, 0

win_status = []  # team1 이 이기고 있다면 1, team2 면 2, 비기는 상태이면 0
time_status = []

for i in range(n):
    team, time = input().split()

    if team == '1':
        t1_score += 1

    else:
        t2_score += 1

    if t1_score > t2_score:
        win_status.append(1)

    elif t1_score < t2_score:
        win_status.append(2)

    else:
        win_status.append(0)

    time_status.append(time)

team1_idx = 0
team2_idx = 0

is_winning = 0

for i in range(n):
    if win_status[i] == 1 and is_winning == 0:
        team1_idx = i
        is_winning = 1


    elif win_status[i] == 2 and is_winning == 0:
        team2_idx = i
        is_winning = 2


    elif win_status[i] == 0:
        # 이 때 시간 계산!!
        time = time_status[i]
        draw_min = int(time.split(":")[0])
        draw_sec = int(time.split(":")[1])

        if is_winning == 1:
            team_time = time_status[team1_idx]
            team_min = int(team_time.split(":")[0])
            team_sec = int(team_time.split(":")[1])

            if draw_sec - team_sec < 0:
                t1_min += (draw_min - team_min - 1)
                t1_sec += (60 + draw_sec - team_sec)
            else:
                t1_min += (draw_min - team_min)
                t1_sec += (draw_sec - team_sec)

        elif is_winning == 2:
            team_time = time_status[team2_idx]
            team_min = int(team_time.split(":")[0])
            team_sec = int(team_time.split(":")[1])

            if draw_sec - team_sec < 0:
                t2_min += (draw_min - team_min - 1)
                t2_sec += (60 + draw_sec - team_sec)
            else:
                t2_min += (draw_min - team_min)
                t2_sec += (draw_sec - team_sec)

        is_winning = 0

team_time = time_status[len(time_status) - 1]
team_min = int(team_time.split(":")[0])
team_sec = int(team_time.split(":")[1])

if is_winning == 1:

    if 0 - team_sec < 0:
        t1_min += (48 - team_min - 1)
        t1_sec += (60 - team_sec)

    else :
        t1_min += (48 - team_min)

elif is_winning == 2:
    if 0 - team_sec < 0:
        t2_min += (48 - team_min - 1)
        t2_sec += (60 - team_sec)

    else:
        t2_min += (48 - team_min)

if t1_min < 10 :
    print("0" + str(t1_min) + ":",end="")
else :
    print(str(t1_min) + ":", end="")

if t1_sec < 10 :
    print("0" + str(t1_sec))
else :
    print(str(t1_sec))

if t2_min < 10 :
    print("0" + str(t2_min) + ":",end="")
else :
    print(str(t2_min) + ":", end="")

if t2_sec < 10 :
    print("0" + str(t2_sec))
else :
    print(str(t2_sec))