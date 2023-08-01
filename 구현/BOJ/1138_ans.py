# 분명 맞는 것 같은데..뭐가 문제지 내 풀이에서
#https://suri78.tistory.com/205
n = int(input())
h = list(map(int, input().split()))
ans = [0] * n
for p in range(1, n+1):
    t = h[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)

# pop , insert가 아닌, 그냥 세워주는 방법
