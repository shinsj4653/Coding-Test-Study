# ds : 문자열
# algo : 탐색?

import sys, math
from collections import defaultdict, Counter

input = sys.stdin.readline

string = input().rstrip()

# counting star -> map 또는 배열
# map 으로 각 문자 갯수 카운트
# 카운트한 결과로 판단?

# 모두 짝수거나, 딱 하나만 홀수
# AAKKK -> 이때는 KAKAK 가 되어야 하는데
# -> 해당 케이스에 대한 반례 처리를 모르겠음

s_dict = defaultdict(int)
s_counter = Counter(string)


for s in string :
    if s not in s_dict :
        s_dict[s] = 1
    else :
        s_dict[s] += 1

odd_cnt = 0

ans = ['A' for _ in range(len(string))]
print(s_dict.keys())
print(ans)

for v in s_dict.values() :
    if v % 2 != 0 :
        odd_cnt += 1

if odd_cnt > 1 :
    print("I'm Sorry Hansoo")


else :
    l_stack = list(s_dict.keys())
    l_stack.sort()
    # 'A' : 3, 'B' : 2
    l_stack_idx = 0

    for i in range(len(ans)) :

        if len(ans) % 2 == 0 :
            if i >= len(ans) // 2 :
                break

        else :
            if i >= len(ans) // 2 + 1 :
                break

        if s_dict[l_stack[l_stack_idx]] <= 1 :
            l_stack_idx = (l_stack_idx + 1) % len(l_stack)

        ans[i] = l_stack[l_stack_idx]
        ans[len(ans) - 1 - i] = l_stack[l_stack_idx]

        s_dict[l_stack[l_stack_idx]] -= 2

    for a in ans :
        print(a, end="")
print()
print((5 // 2) - 1)















