# https://velog.io/@daeungdaeung/%EB%B0%B1%EC%A4%80-17266-%EC%96%B4%EB%91%90%EC%9A%B4-%EA%B5%B4%EB%8B%A4%EB%A6%AC-with-Python

# 가로등이 배열 인덱스 위치가 아니라 인덱스 사이사이에 있다고 당황 x
# 필요한 정보, 즉 높이만을 계산하면 되니까 필요한 정보만 뽑아온다는 생각으로 풀이에 임하기
n = int(input())
m = int(input())

positions = list(map(int, input().split()))
len_positions = len(positions)

min_height = 0

# 가로등 하나 있는 경우
if len_positions == 1 :
    min_height = max(positions[0] - 0, n - positions[0])

# 가로등이 하나 이상 있는 경우
else :
    for i in range(len_positions) :
        # 입구 근처의 첫번째 가로등이 비춰줘야할 거리
        if i == 0 :
            height = positions[i] - 0

        # 끝나는 지점 기준 가장 가까운 가로등이 비춰줘야할 거리
        elif i == len_positions - 1 :
            height = n - positions[i]

        # 양 끝 제외한 가로등 -> 이 방법을 생각 못함
        else :
            tmp = positions[i] - positions[i - 1]
            if tmp % 2 :
                height = tmp // 2 + 1
            else :
                height = tmp // 2
        # 가장 큰 범위를 찾으면 됨!
        min_height = max(height, min_height)


print(min_height)