# 다시 되돌아갈 때, 체스판을 어떻게 설정해줘야 할지 감이 잘 안왔음
# 그리고, is_used = [False] * n 으로 할 지, 아니면 append, pop 으로 해야할지도 모르겠음
# 문제 유형에 익숙해지기 위해 답 확인

# 각 행에 퀸이 딱 1개씩 있어야 한다 -> 핵심 아이디어
answer = 0
n = int(input())

# 퀸의 열 판별 배열
isused1 = [0] * 40

# 왼아래, 우위 방향 대각선 배열 -> x + y
isused2 = [0] * 40

# 왼위, 우아래 방향 대각선 배열 -> x - y + n - 1
isused3 = [0] * 40

def func(cur) :
    global answer
    if cur == n :
        answer += 1
        return

    for i in range(n) :
        if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1] :
            continue
        isused1[i] = 1
        isused2[i + cur] = 1
        isused3[cur - i + n - 1] = 1
        func(cur + 1)
        isused1[i] = 0
        isused2[i + cur] = 0
        isused3[cur - i + n - 1] = 0

func(0)
print(answer)