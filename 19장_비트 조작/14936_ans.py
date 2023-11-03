# 앞서 내 풀이 -> 동작들을 이진화 시킨 방법
# 이거의 베스트 풀이를 한번 봐야 더 감이 잘 올 것 같음

import sys
n, m = map(int, sys.stdin.readline().split())

ans = 1 # 모두 꺼진 상태

a = (n / 2) + 1
if n % 2 == 0 :
    a = n / 2

b = n / 2
c = n / 3
if n % 3 >= 1 :
    c = n / 3 + 1

if n <= m :
    ans += 1

if a <= m and n > 1 :
    ans += 1

if b <= m and n > 1 :
    ans += 1

if c <= m and n > 2 :
    ans += 1

if c + a <= m and n > 2 :
    ans += 1

if c + b <= m and n > 2 :
    ans += 1

if c + n <= m and n > 2 :
    ans += 1

print(ans)

