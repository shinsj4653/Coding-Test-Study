# 예전에 실패한 문제
# 이번엔 성공해보자!

# 1번team cnt, 2번 팀cnt, 1time, 2time
# 이전 시간 => prev 이용
# for i in range(n) ;
# if i > 0 :
#   if 1cnt > 2cnt
#       1time += 지금시간 - 이전시간

prev_min, prev_sec = 0, 0
cnt1, cnt2 = 0, 0 # 득점 수
min_1, sec_1, min_2, sec_2 = 0, 0, 0, 0 # 이기고 있던 시간

n = int(input())
for i in range(n) :
    team, time = input().split(" ")

    cur_min, cur_sec = map(int, time.split(":"))
    #print(cur_min, cur_sec)

    if i > 0 :
        if cnt1 > cnt2:
            if cur_sec - prev_sec >= 0 :
                min_1 += cur_min - prev_min
                sec_1 += cur_sec - prev_sec

            else :
                # 분에서 내림해야됨
                min_1 += cur_min - 1 - prev_min
                sec_1 += 60 - prev_sec + cur_sec

        elif cnt1 < cnt2 :
            if cur_sec - prev_sec >= 0 :
                min_2 += cur_min - prev_min
                sec_2 += cur_sec - prev_sec

            else :
                # 분에서 내림해야됨
                min_2 += cur_min - 1 - prev_min
                sec_2 += 60 - prev_sec + cur_sec

    if team == '1' :
        cnt1 += 1
    else:
        cnt2 += 1

    prev_min, prev_sec = cur_min, cur_sec

if cnt1 > cnt2:
    if prev_sec == 0 :
        min_1 += 48 - prev_min

    else:
        # 분에서 내림해야됨
        min_1 += 48 - 1 - prev_min
        sec_1 += 60 - prev_sec

elif cnt1 < cnt2:
    if prev_sec == 0:
        min_2 += 48 - prev_min

    else:
        # 분에서 내림해야됨
        min_2 += 48 - 1 - prev_min
        sec_2 += 60 - prev_sec


print("0" + str(min_1) + ":", end="") if min_1 < 10 else print(str(min_1) + ":", end="")
print("0" + str(sec_1)) if sec_1 < 10 else print(str(sec_1))
print("0" + str(min_2) + ":", end="") if min_2 < 10 else print(str(min_2) + ":", end="")
print("0" + str(sec_2)) if sec_2 < 10 else print(str(sec_2))