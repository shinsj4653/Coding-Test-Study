# https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-1593%EB%B2%88-%EB%AC%B8%EC%9E%90-%ED%95%B4%EB%8F%85-Python-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%94%A9-%EC%9C%88%EB%8F%84%EC%9A%B0

g, s = map(int, input().split())
W = input()
S = input()

answer = 0
wa = [0] * 58
sa = [0] * 58

for x in W :
    wa[ord(x) - 65] += 1

# 구간 비교를 시작할 시작점 start와 현재 카운팅한 알파벳 길이 length를 초기화하고 시작
start, length = 0, 0
for i in range(s) :
    sa[ord(S[i]) - 65] += 1
    length += 1

    if length == g :
        if wa == sa :
            answer += 1
        sa[ord(S[start]) - 65] -= 1
        start += 1
        length -= 1

print(answer)
