# 짝짓기 -> 스택?
# flag 변수 0, 1 둬서 계산 한다 안한다 로 하려 했지만
# 1 + 2 + 3
# -> 여기서 1 + 2 혹은 2 + 3만 괄호가 가능
# 그래서 0, 1 재귀로 불가능할듯

# 계산하고 나면 무조건 다음은 pass하기로?


from collections import deque

ret = 2**31 * (-1)

nums = deque()
cals = deque()

n = int(input())
s = input()

for i in range(n) :
    if s[i].isdigit():
        nums.append(int(s[i]))

    else :
        cals.append(s[i])

st = deque()

def go(prev, next, cal) :
    if cal == "+" :
        return prev + next

    elif cal == "-" :
        return prev - next

    else :
        return prev * next

def solve(nums, cals, st, flag) :
    global ret

    if len(nums) <= 1 :

        copy_nums = deque()
        copy_cals = deque()

        for ss in st :
            if str(ss).isdigit():
                copy_nums.append(int(ss))

            else:
                copy_cals.append(ss)

        if len(nums) == 1 :
            copy_nums.append(nums[-1])

        cur = int(copy_nums.popleft())

        while len(copy_nums) > 0 :
            result = go(cur, int(copy_nums.popleft()), copy_cals.popleft())
            cur = result

        ret = max(ret, cur)
        return

    if flag : # 계산 후 sum_num 업데이트
        # if len(st) == 0: # st에 없을 때
        #     l = nums.popleft()
        #
        # else :
        #     l = st.pop()
        l = nums.popleft()
        r = nums.popleft()
        cal = cals.popleft()

        result = go(l, r, cal)
        st.append(result)

        solve(nums, cals, st,0) # 한번 계산후엔 무조건 pass 하는 메타로

    else : # 계산 하지 않고 그대로 st에 넣기
        cur = nums.popleft()
        cal = cals.popleft()

        st.append(cur)
        st.append(cal)

        solve(nums, cals, st, 0)

        # # 원복
        nums.appendleft(cur)
        cals.appendleft(cal)
        #
        st.pop()
        st.pop()

        solve(nums, cals, st, 1)

if n == 1 :
    print(nums[0])
else :
    solve(nums, cals, st, 0)
    solve(nums, cals, st, 1)
    print(ret)


#8 3 4
#+ *

#   0      1
#  0  1  0
# 0 1 0 0 1