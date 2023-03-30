import sys

n, m = map(int, input().split())
ans = 0
result = []

for i in range(n) :
    students, max_student = map(int, input().split())

    # sorted 사용법
    m_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    if students < max_student :
        result.append(1)

    else :
        result.append(m_list[max_student - 1])

result.sort()
cnt = 0
for i in result :
    m -= i
    cnt += 1
    if m < 0 :
        print(cnt - 1)
        break

if m > 0:
    print(cnt)

