import sys
from collections import defaultdict

input = sys.stdin.readline

string = input().rstrip()

# 홀수가 2개 이상이면 불가능
# -> 이건 떠올리기 쉬움

# 가운데 부터 아스키코드상 값이 높은 거 부터 배열해야 사전순 조건 만족
# mid를 뽑아두고, 나머지는 "가운데부터" 2씩 추가
# 꼭 왼쪽부터 할 생각 안해도 될듯..가운데부터 갖다 붙이는 식으로 해도 될듯!
# 파이썬의 장점을 잘 활용해보자

ret = ''

cnt = defaultdict(int)

for s in string :
    if s not in cnt :
        cnt[s] = 1
    else :
        cnt[s] += 1

c_keys = list(cnt.keys())
c_keys.sort(reverse=True)

flag = 0
mid = ''

for i in c_keys :
    if cnt[i] & 1 :
        mid = i
        flag += 1
        cnt[i] -= 1

    if flag == 2 :
        break

    for j in range(0, cnt[i], 2) :
        ret = i + ret
        ret += i

ans = ''

if mid :
    ans = ret[:len(ret) // 2] + mid + ret[len(ret) // 2:]

else :
    ans = ret

print("I'm Sorry Hansoo") if flag == 2 else print(ans)
