# Parametric Search
# (최적화 문제) : N개를 만들 수 있는 랜선의 최대 길이
# (결정 문제) : 랜선의 길이가 X 일때, 랜선이 N개 이상인가 아닌가?

import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
wires = []

for i in range(k) :
    wires.append(int(input()))

def binary_search(start, end) :

    while start < end :
        w_len = (start + end + 1) // 2
        total = 0

        for w in wires :
            total += w // w_len

        if total < n : # 그만큼 전선의 길이를 줄여야 함
            end = w_len - 1

        elif total >= n :
            start = w_len

    return start

print(binary_search(1, max(wires)))