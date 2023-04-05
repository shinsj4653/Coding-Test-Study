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
    












