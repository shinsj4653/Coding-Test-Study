# 5:46 ~ 6:10 (o)

# 그룹 수의 최댓값 -> 오름차순 정렬 후, 작은 수 부터 카운팅 해야 그룹이 많이 생길듯
# 하지만, 문제 입력 예시에 (1,2,3),(2,2) 가 나옴
# 그래도 (1), (2,2)
# 그럼 내림차순, 오름차순 정렬해서 계산한 결과를 서로 비교해야하나?

# n 최댓값 100000
# n^2 -> 10000000000 -> 2중 for문 불가능


N = int(input())
fears = list(map(int, input().split()))

fears.sort(reverse=True)

result = 0

# 1 2 2 2 3 오름차순은 계산이 안될 것 같음
# 2 인데 다음 숫자가 3이면 어떡함
# 내림차순이 맞을 것 같은데..이게 최대 그룹을 만들어줄지는 모르겠음...
# 3 2 2 2 1

cur_fear = 1
cur_idx = 0

while cur_idx < len(fears) :
    cur_fear = fears[cur_idx]
    cur_idx += cur_fear
    result += 1

print(result)


# 정답
# 오름차순 정렬
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도를 낮은 것 부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 포험가 포함
    if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 생성!
        result += 1 # 총 그룹의 수 증가
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화



