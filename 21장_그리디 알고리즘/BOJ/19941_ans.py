# https://coder38611.tistory.com/133
# 전에 내가 했던 풀이에서는 start, end 정할 때 살짝 문제가 있는 것 같다.
# max, min 사용하여 인덱스 범위 정하기로 해결

n, k = map(int, input().split())
placement = list(input())
ans = 0
for idx in range(n):
    if placement[idx] == 'P':
        for i in range(max(idx-k, 0), min(idx+k+1, n)):
            if placement[i] == 'H':
                placement[i] = 0
                ans += 1
                break
print(ans)