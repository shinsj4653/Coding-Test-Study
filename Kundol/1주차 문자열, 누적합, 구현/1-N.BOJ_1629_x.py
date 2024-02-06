# logaX = b
# a를 b번 곱하면 X
# 11 -> 5 5 1
# 2 2 1 2 2 1
# 1 1 1 1  1 1  1 1

# 재귀 -> 시간 초과
#

import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())

def mul(a, b, c) :

    if b == 1 :
        return a

    if b % 2 != 0 :
        return mul(a, (b // 2) % c, c) * mul(a, (b // 2) % c, c) * mul(a, 1, c)

    else :
        return mul(a, (b // 2) % c, c) * mul(a, (b // 2) % c, c)

ans = mul(a, b, c)
print(ans % c)