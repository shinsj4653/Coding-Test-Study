# 6:52 ~ 풀이 시간 초과

# 0001100 -> 뒤집기 최소 횟수
# 2초 : S길이 100만보다 작다.
# 2중 for문 x

# 0만 뒤집는 경우, 1만 뒤집는 경우 비교
# 근데, 복사를 해둬야 0, 1 2가지 방법으로 비교할 수 있는거 맞나?

# "재할당" 해야하므로, 문자열 대신 리스트사용

import copy

zero_s = list(input()) # 0 -> 1

z_cnt = 0
o_cnt = 0

one_s = copy.deepcopy(zero_s)


while zero_s.count('0') > 0 :
    print('zero_s : ', zero_s)
    start_idx = zero_s.index('0') # '0'의 첫 위치 찾기
    end_idx = start_idx

    while end_idx + 1 < len(zero_s) :
        if zero_s[end_idx + 1] == '0' : # 다음이 '1' 이 아니면 '0'임
            end_idx += 1
        else:
            break

    for i in range(start_idx, end_idx + 1) :
        zero_s[i] = '1'

    z_cnt += 1

while one_s.count('1') > 0 :
    print('one_s : ', one_s)
    start_idx = one_s.index('1') # '1'의 첫 위치 찾기
    end_idx = start_idx

    while end_idx + 1 < len(one_s) :
        if one_s[end_idx + 1] == '1' : # 다음이 '0' 이 아니면 '1'임
            end_idx += 1
        else:
            break

    for i in range(start_idx, end_idx + 1) :
        one_s[i] = '0'

    o_cnt += 1

print(min(z_cnt, o_cnt))

# 정답
# 전부 0으로 바꾸는 경우랑 전부 1로 바꾸는 경우 비교하는 건 맞음
# for문 한번으로 비교할 수 있는 방법 존재!
# 현재수랑 다음수랑 비교해서 달라진다면, 그 부분만 체크하면 됨! 덩어리로 묶어서 생각

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1' :
    count0 += 1
else :
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인
for i in range(len(data) - 1) :
    if data[i] != data[i + 1] :
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1' :
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else :
            count1 += 1

print(min(count0, count1))