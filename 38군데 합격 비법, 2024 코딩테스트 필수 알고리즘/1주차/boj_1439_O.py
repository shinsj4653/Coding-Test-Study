# n : 최대 10^7
# o(n^2) 불가능

# 쭉 돌면서
# [(숫자, 출발지점, 연속 개수), ]
# -> 0, 1 묶음 카운트 해서, 더 적은걸로
# cnt_1, cnt_0

# li_1 = [(3)]
# li_0 = [(0) (5)]

# 0 혹은 1 이 시작하는 지점을 각 리스트에 넣고,
# total cnt 값이 더 적은 쪽의 리스트 len 구하면 끝 아닌가?

import sys

input = sys.stdin.readline
s = input()

def find_least_cnt(s) :
    if len(s) == 0 or len(s) == 1 :
        return 0

    li = [0, 0]

    c = s[0]
    li[int(c)] += 1

    for idx in range(1, len(s)) :
        if c != s[idx] :
            li[int(c)] += 1
            c = s[idx]

    return min(li)


print(find_least_cnt(s))