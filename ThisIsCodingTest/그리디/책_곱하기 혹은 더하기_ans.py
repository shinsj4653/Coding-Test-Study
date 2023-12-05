# 6:12 ~ 6:51 (o)

# 0이면 당연히 + , 나머지는 * 가 수 커짐

# 1차원 for문 -> S의 두번째부터 시작
# 전 숫자 보면서 0이면 +, 아니면 * 해서 수 업데이트


s = list(map(int, input()))
print(s)

if len(s) == 1 :
    print(s[0])

idx = 1
result = s[idx - 1]

while idx < len(s) :
    if int(s[idx - 1]) == 0 :
        result += s[idx]

    else :
        result *= s[idx]

    idx += 1

print(result)

# 정답
# 1일때도 고려해야함 -> 1일 때도 * 보다 + 가 더 효율적
# 그래서, 두 수 중에서 하나라도 1이하인 경우에는 더하며, 두 수가 모두 2이상인 경우엔 곱하면 된다.

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)) :
    # 두 수 중에서 하나라도 '0' 혹은 '1' 인 경우, 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else :
        result *= num

print(result)