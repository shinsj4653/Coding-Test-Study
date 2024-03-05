# 1. 누적합 idx 를 기준으로 탐색
# 2. +, * 이랑 3, 8 구분

# 완탐할때는 idx 기반으로 탐색한다고 생각
# -> dag 기반

# 넘버와 기호 나눈 아이디어는 맞음

# 짝짓기 == 스택
# 하지만, 이번 에는 idx로 해결

# 결론
# 하나의 방향만 있는 그래프 -> 인덱스 및 누적합으로 해결

from collections import deque

num = deque()
open_str = deque()

n = int(input())
string = input()
ret = -1 * (2 ** 31)

for i in range(len(string)) :
    if i % 2 == 0 :
        num.append(int(string[i]))
    else :
        open_str.append(string[i])


def oper(prev, next, cal) :
    if cal == "+" :
        return prev + next

    elif cal == "-" :
        return prev - next

    else :
        return prev * next

def go(here, _num) :
    global ret

    if here == len(num) - 1 :
        ret = max(ret, _num)
        return

    go(here + 1, oper(_num, num[here + 1], open_str[here]))

    if here + 2 <= len(num) - 1 :
        temp = oper(num[here + 1], num[here + 2], open_str[here + 1])
        go(here + 2, oper(_num, temp, open_str[here]))


go(0, num[0])
print(ret)