# ds : counting star -> map
# algo : iter

# 아치형 곡선 교차하지 않도록
# 만약 카운트 배열 내에 홀수 숫자 있다면 x

# 겹치는지 판별 -> 스택
# 스택의 맨 끝이랑 다음 문자 같으면 pop(), pop()
# 스택 길이가 0 이어야 가능

# 딱히 카운트 배열 없어도 될듯


# -- 답 --
# 문자열 : 도저히 발상이 안되면?
# 뒤집어보거나, 하나를 더 붙이거나, 90도 회전하거나
# 예시 보고 이해안되면 도식화 해보기!
# -> 세로로 그렸을 때,
# A
# B
# B
# A
# -> B 끼리 폭발한 다음, A 끼리 만나서 또 폭발
# -> 이런 아이디어 캐치 가능
# 가장 뒤에 있는 것만 체크 -> 스택 떠올리기!
# 큐는 가장 앞에 있는 것이므로 스택 사용

# 스택, 큐 -> 가장 뒤 혹은 앞 체크 할때
# -> size 꼭 체크해야함!

# 만약, 짝짓기 혹은 폭발이면
# -> 스택을 생각해보기!

import sys
input = sys.stdin.readline

n = int(input())
st = []
ans = 0

for i in range(n) :
    string = input().rstrip()

    for i in range(len(string)) :
        st.pop() if len(st) > 0 and st[-1] == string[i] else st.append(string[i])

    if len(st) == 0 :
        ans += 1

    st = []

print(ans)
