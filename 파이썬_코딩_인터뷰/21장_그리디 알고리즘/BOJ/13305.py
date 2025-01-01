# 가격이 비싸면 최대한 적게 넣고, 싸면 많이 넣기?

import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
min_price = min(price[0:len(price) - 1])

for i in range(len(price) - 1) :
    if price[i] == min_price :
        for j in range(i, len(road)) :
            ans += price[i] * road[j]
        break

    else :
        ans += price[i] * road[i]
print(ans)