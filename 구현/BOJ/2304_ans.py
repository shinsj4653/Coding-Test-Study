# https://recordofwonseok.tistory.com/409
# 최고 높이 기준으로 나눠서 생각하는 건 맞음
# 이 사람은 더하는 방식으로 풀었다
# 기둥 가로 길이가 1인 것을 활용!
# 하나의 pli 리스트를 추가로 만들어서 활용

import sys
input = sys.stdin.readline

m = 0
m_idx = 0
pli = [0 for _ in range(1001)] #기둥
for _ in range(int(input())) :
    l, h = map(int, input().split())
    pli[l] = h
    if m < h : # 가장 높은 기둥과 그 기둥의 인덱스 저장
        m_idx = l
        m = h

curr = 0
ans = 0
for i in range(m_idx + 1) : #왼쪽 그룹
    curr = max(curr, pli[i])
    ans += curr

curr = 0
for i in range(1000, m_idx, -1) : #오른쪽 그룹
    curr = max(curr, pli[i])
    ans += curr

print(ans)