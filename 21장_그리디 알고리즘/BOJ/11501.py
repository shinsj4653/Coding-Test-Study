import sys
from collections import deque # deqeu 생성법 외워라...
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    n = int(input())
    p_list = deque(map(int, input().split()))

    profit = 0

    # 젤 높을 때 팔기
    max_price = max(p_list)
    for i in range(n) :
        price = p_list.popleft()
        if price < max_price :
            profit += (max_price - price)
        if len(p_list) > 0 :
            max_price = max(p_list)

    print(profit)



