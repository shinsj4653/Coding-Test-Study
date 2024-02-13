# 맞왜틀
# 분과 초로 주어지면?
# -> 하나의 단위로 통일하자 (낮은 단위 추천)
# 통일해서 계산하니 정답이다..

# 이 문제 중요 뽀인트
# 1. prev를 통한 시간 간격 게산
# 2. 시간 여러 단위면, 작은 단위 기반으로 통일하자
# 3. 출력할 때, "00" 붙여서 끝에서 2개만 가져오는 식으로 포맷화하기

def print_time(time) :
    m = "00" + str(time // 60)
    s = "00" + str(time % 60)
    return m[len(m) - 2:len(m)] + ":" + s[len(s) - 2:len(s)]

prev_time = 0
cnt1, cnt2 = 0, 0 # 득점 수
time1, time2 = 0, 0 # 1팀, 2팀 이기고 있던 초 수
min_1, sec_1, min_2, sec_2 = 0, 0, 0, 0 # 이기고 있던 시간

n = int(input())
for i in range(n) :
    team, time = input().split(" ")

    cur_min, cur_sec = map(int, time.split(":"))
    cur_time = cur_min * 60 + cur_sec

    if i > 0 :
        if cnt1 > cnt2:
            time1 += cur_time - prev_time

        elif cnt1 < cnt2 :
            time2 += cur_time - prev_time

    if team == '1' :
        cnt1 += 1
    else:
        cnt2 += 1

    prev_time = cur_time
# 48:00 -> 48 * 60

if cnt1 > cnt2:
    time1 += 48 * 60 - prev_time

elif cnt1 < cnt2:
    time2 += 48 * 60 - prev_time

min_1 = time1 // 60
sec_1 = time1 % 60

min_2 = time2 // 60
sec_2 = time2 % 60 # 몫을 빼는 방식 말고 mod 연산 활용하자

# print("0" + str(min_1) + ":", end="") if min_1 < 10 else print(str(min_1) + ":", end="")
# print("0" + str(sec_1)) if sec_1 < 10 else print(str(sec_1))
# print("0" + str(min_2) + ":", end="") if min_2 < 10 else print(str(min_2) + ":", end="")
# print("0" + str(sec_2)) if sec_2 < 10 else print(str(sec_2))
# 너무 로직 길면 따로 출력하는 함수 빼서 사용

print(print_time(time1))
print(print_time(time2))