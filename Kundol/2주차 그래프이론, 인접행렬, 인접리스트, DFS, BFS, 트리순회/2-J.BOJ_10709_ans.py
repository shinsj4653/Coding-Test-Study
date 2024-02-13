h, w = map(int, input().split())

a = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
#print(a)

# 우선 c있으면 0 아니면 -1로 초기화
# 입력받는 즉시 값 세팅 하는 방식도 존재

for i in range(h) :
    s = input()
    for j in range(w) :
       if s[j] == '.' :
           a[i][j] = -1

       else :
           a[i][j] = 0


for i in range(h) :
    for j in range(w) :
        if a[i][j] == 0 :
            cnt = 1
            while a[i][j + 1] == -1 :
                a[i][j + 1] = cnt
                cnt += 1
                j += 1

for i in range(h) :
    for j in range(w) :
        print(a[i][j], end=" ")
    print()

