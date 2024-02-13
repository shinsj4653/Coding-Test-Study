# 전꺼랑 비교하면서 탐색
# for i in range(len(input())
# -> 소문자면 continue
# -> 숫자고, 앞에 소문자면 기록
# -> 숫잔데 0이면 continue
# -> 단 0인데 마지막이면 리스트에 보관
# -> 기록하다가 이번게 문자면 기록했던 숫자 리스트에 보관

nums = [] # 맨 나중에 오름차순 정렬

# 반례: 202 가 중간에 낄 경우

n = int(input())

for i in range(n) :
    s = input()
    prev = ''

    for j in range(len(s)) :
        if s[j].isdigit() :
            prev += s[j]

        elif s[j].isalpha() and prev != '' :
            nums.append(int(prev))
            prev = ''

    if prev != '' :
        nums.append(int(prev))

nums.sort()
for num in nums :
    print(num)
