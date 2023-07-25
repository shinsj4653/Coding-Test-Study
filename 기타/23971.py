h, w, n, m = map(int, input().split())
# 세로로 n칸, 또는 가로로 m칸 이상

ans = 0
# 파이썬 2차원 배열 생성 - https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0
#c = [[0 for j in range(w)] for i in range(h)]
w_cnt = 0 # 가로 여백
h_cnt = 0 # 세로여백

row_cnt = 0 # 가로 자리 갯수

for j in range(w) :

    if j == 0:
        row_cnt += 1

    elif w_cnt == m :
        w_cnt = 0
        row_cnt += 1

    else :
        w_cnt += 1

ans += row_cnt

for i in range(1, h) :
    
    if h_cnt == n :
        ans += row_cnt
        h_cnt = 0
    
    else :
        h_cnt += 1

print(ans)

# 더 좋은 풀이
# https://velog.io/@qwerty1434/%EB%B0%B1%EC%A4%80-23971%EB%B2%88-ZOAC-4
# math.ceil() 함수와 "강의실 길이 / (띄어앉아야하는 칸 수 + 1) 을 올림하는 규칙성을 활용하여 문제를 풀었다.

# 2차원 배열 생성
# https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0
# '*' : 파이썬에서 얕은 복사. 깊은 복사를 위해서는 위의 코드처럼 선언해야한다.











