# 순열 결과들 -> 어떻게 조회 ??
# https://velog.io/@ryucherry/Python-%EC%88%9C%EC%97%B4permutations%EA%B3%BC-%EC%A1%B0%ED%95%A9combinations%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
# list 화 시켜야한다

# 메모리 초과 문제 어떻게 해결??
# 

from itertools import permutations
import sys
input = sys.stdin.readline

g, s = map(int, input().split())
W = input().strip()
S = input().strip()

answer = 0
permutation_list = list(permutations(W, 4))

for i in range(s - g + 1) :
    sliced_S = S[i:i + 4]

    for p in permutation_list :
        if ''.join(p) == sliced_S :
            answer += 1
            break

print(answer)