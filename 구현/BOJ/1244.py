# 1. 문제를 꼼꼼히 읽자
# 출력 형식까지 꼼꼼하게 읽어야 문제 맞추기 가능!

# 2. int(not False) => 1
# not 과 int 를 활용하여 0, 1 의 스위칭이 가능하다.

import sys

s = int(input())
s_list = list(map(int, sys.stdin.readline().split()))

n = int(input())

for i in range(n) :
    g, num = map(int, input().split())

    if g == 1 :
        for j in range(len(s_list)) :
            if (j + 1) % num == 0 :
                s_list[j] = int(not s_list[j])

    else :
        left, right = num - 2, num

        while left > -1 and right < len(s_list) :
            if s_list[left] == s_list[right] :
                left -= 1
                right += 1
            else :
                break

        if left < 0 :
            for j in range(0, right) :
                s_list[j] = int(not s_list[j])

        elif right >= len(s_list) :
            for j in range(left + 1, len(s_list)) :
                s_list[j] = int(not s_list[j])

        else :
            for j in range(left + 1, right) :
                s_list[j] = int(not s_list[j])

for s in range(len(s_list)) :
    print(s_list[s], end=" ")
    if (s + 1) % 20 == 0 :
        print()
