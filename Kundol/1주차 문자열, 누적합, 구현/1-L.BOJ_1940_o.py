# 조합 문제
# 2개에 대한 조합

# ds : stack
# algo : 재귀

# 2^15000
# -> 과연 2초안에 가능할지

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ingre = list(map(int, input().split()))
ans = 0

# 1. 예외처리 중요!
if m > 200000 :
    print(0)
    exit()
# 번호가 최대 100000 -> m이 20만 넘으면 애초에 안됨

# 2. 3개까지는 단순 for문으로 구현하는 것이 더 편리
def comb(start, b) :
    global ingre
    global ans

    if len(b) == 2 :
        if sum(b) == m :
            ans += 1
        return

    for i in range(start + 1, n) :
        b.append(ingre[i])
        comb(i, b)
        b.pop()

b = []
comb(-1, b)
print(ans)