# 문제 이해 이슈..
# 문자들을 재배치 할 수는 없다...
# 그리디적으로 생각! -> 0은 최대한 앞만 남기면 되고, 1은 최대한 뒤만 남기면 된다.

s = input()
z_cnt = 0
o_cnt = 0

z_idx = 0
o_idx = 0

mark_idx = 0

s_list = []

def slice_operate(s, z_cnt, o_cnt, o_idx) :
    if len(s) == 0:
        return
    elif len(s) == 1 or len(s) == 2:
        s_list.append(s)
        return
    else :
        for cur_idx in range(len(s)):
            if s[cur_idx] == '0':
                z_cnt += 1
            else:
                o_cnt += 1

            if z_cnt == 2:
                print(s[:cur_idx])
                print(s[cur_idx + 1:])
                slice_operate(s[:cur_idx], 0, 0, 0)
                slice_operate(s[cur_idx + 1:], 0, 0, 0)

            elif o_cnt == 2:
                print(s[:o_idx])
                print(s[o_idx + 1:])
                slice_operate(s[:o_idx], 0, 0, 0)
                slice_operate(s[o_idx + 1:], 0, 0, 0)

            if s[cur_idx] == '1':
                o_idx = cur_idx

slice_operate(s, z_cnt, o_cnt, o_idx)

print(s_list)


# z_cnt, o_cnt
# 만약, z_cnt나 o_cnt가 2
# last index 부터 cur_idx 까지 자르기
# 단, 0은 뒤에꺼 자르기, 1은 앞에꺼 자르기

# 0일때는 처음부터 cur_idx, cur_idx과 마지막 0인 위치 전까지
# 1일때는 마지막1인 위치다음부터

# 그런데 이걸 계속 단계별로 들어가면서 상태값도 저장해야해서..그럼 재귀를 써야하나??


