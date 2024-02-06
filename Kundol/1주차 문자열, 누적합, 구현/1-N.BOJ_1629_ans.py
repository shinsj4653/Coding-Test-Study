# 재귀 -> 시간 초과
# 문제의 최대 범위를 항상 생각해라
# 2중 for문 -> 20억 * 20억 -> 0.5 초 절대불가능
# 매번 곱하는 거에 대한 시간 복잡도를 어떻게 줄일 수 있을까?
# -> 문제로 푸는 로그 연산

# mod 연산 -> (a * a * a) % c
# -> 얘를 (a % c) * (a % c) * (a % c)
# -> 이런식으로 최적화

import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())

def go(a, b) :
    if b == 1 :
        return a % c

    ret = go(a, b // 2)
    ret = (ret * ret) % c
    if b % 2 == 1 :
        ret = (ret * a) % c
    return ret

print(go(a, b))

# 2를 5번

# 2 5 -> go(2, 2) 4 4 * 2
# 2 2 -> 4
# go(2, 1) ret 2



