#https://kkk4872.tistory.com/139
# 가끔 안 풀리면??반대로 생각해봐라

import sys
from collections import deque # deque 생성법 외워라...
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    n = int(input().strip())
    p_list = list(map(int, input().strip().split()))

    profit = 0

    # 젤 높을 때 팔기
    max_price = 0
    for i in range(n - 1, -1, -1) :
        if p_list[i] > max_price :
            max_price = p_list[i]
        else :
            profit += (max_price - p_list[i])

    print(profit)


