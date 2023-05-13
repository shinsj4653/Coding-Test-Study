# 미리 값 정하고 그 다음에 for문 순회
# 풀이 : https://alpyrithm.tistory.com/68
# 입력값들 내에서 "규칙"을 찾아보자
# 먼저 res 값 정하고, for문 돌면서 해당 기준에 맞는거 찾으면 값 변경.
# 만약 다 돌았는데 기준에 맞는거 못 찾았으면 처음에 정한 값을 정답으로 처리.

n, new, p = map(int, input().split())
if n == 0 :
    print(1)

else :
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new :
        print(-1)
    else :
        res = n + 1
        for i in range(n) :
            if score[i] <= new :
                res = i + 1
                break
        print(res)