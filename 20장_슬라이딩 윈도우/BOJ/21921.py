# 와..내 블로그가 드디어 빛을 발하네요..
# https://shinsj4653.github.io/CI_Part5_Ch20/
# 슬라이딩 윈도우 개념 정리한거 제대로 써먹은 문제!
# 파이썬 양의 무한대, 음의 무한대 : https://da-nyee.github.io/posts/python-infinity/

import sys
input = sys.stdin.readline

from collections import deque

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

max_num = 0
max_cnt = 0

main_num = 0

d = deque()

for i in range(n) :
    d.append(visitors[i])
    main_num += visitors[i]

    if i < x - 1 :
        continue

    if main_num > max_num :
        max_num = main_num
        max_cnt = 1
    elif main_num == max_num :
        max_cnt += 1

    main_num -= d.popleft()

if max_num == 0:
    print("SAD")
else :
    print(max_num)
    print(max_cnt)




