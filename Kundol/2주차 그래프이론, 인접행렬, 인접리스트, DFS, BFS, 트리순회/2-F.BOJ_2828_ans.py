# 야매로 푼 것 같아서 풀이 보고 정리

# 바구니 왼쪽 l, 오른쪽 r
# r을 l + m - 1 로 설정 가능
# -> 이걸 생각해내기!

n, m = map(int, input().split())
j = int(input())

l = 1
ret = 0

for i in range(j) : # 매 루프마다 r을 재정의
    r = l + m - 1
    a = int(input())

    if l <= a <= r :
        continue

    if a < l :
        ret += l - a
        l = a

    else:
        l += a - l
        ret += a - l

print(ret)