# counting star 는 map 또는 배열
# count 할때 -> 보통 string 기반일 때는 map, int 일때는 배열

# 그럼 이 문제는 문자열이니까? map?
# 아스키코드 쓰면 숫자로 표현 가능

# 알파벳 배열
cnt = [0] * 26

s = input()

for ss in s :
    cnt[ord(ss) - ord('a')] += 1

for c in cnt :
    print(c, end=" ")