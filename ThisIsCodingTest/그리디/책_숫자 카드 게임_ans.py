# 뽑은 행에서 가장 낮은 숫자 고름 => 이것이 전체에선 가장 최대여야 함
# 최댓값 찾기 => max 함수 사용하기!

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

answer = 1

for c in cards :
    min_num = min(c)
    answer = max(min_num, answer)

print(answer)