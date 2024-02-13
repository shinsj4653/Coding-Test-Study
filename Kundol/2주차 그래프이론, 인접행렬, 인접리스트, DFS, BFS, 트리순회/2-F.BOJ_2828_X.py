n, m = map(int, input().split())
# 1차원 bfs?
# 가중치 같은 최소거리
# 근데 문제 이해를 못하겠..
# 입력조건까지 모오오두 끝까지 읽자.
# -> 둘째 줄 부터 사과 위치가 아니라, 둘째 줄에 j가 입력됨

j = int(input())

left = 1
right = m
ret = 0

if m == 1 :
    for k in range(j):
        a = int(input())

        ret += abs(a - left)


        if a - left == 0 :
            continue

        elif a - left > 0 :
            left += abs(a - left)

        else :
            left -= abs(a - left)


    print(ret)

else :
    for k in range(j) :
        a = int(input())

        if left <= a <= right :
            continue

        if abs(left - a) > abs(right - a) : # 오른쪽으로 바구니 이동
            ret += abs(right - a)
            left += abs(right - a)
            right += abs(right - a)

        else :
            ret += abs(left - a)
            right -= abs(left - a)
            left -= abs(left - a)

    print(ret)

# 1 2
# 3
# 4 5