# 집합에 원소 있는지 여부 파악
import sys

S = set()
M = int(input())
for i in range(M) :

    input_str = sys.stdin.readline().strip()
    
    # all, empty 예외처리 해줘야함
    if "all" in input_str or "empty" in input_str:
        if input_str == "all":
            S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

        else:
            S.clear()

    else :
        # split() -> list 를 리턴해줌
        way, _num = map(str, input_str.split())
        num = int(_num)
    
        if way == "add" :
            if num in S :
                continue
            else :
                S.add(num)

        elif way == "remove" :
            if num not in S :
                continue
            else :
                S.remove(num)
            #S.discard(num) # -> 없는 원소 없애려고 해도 오류 안남

        elif way == "check" :
            if num in S :
                print(1)
            else :
                print(0)

        elif way == "toggle" :
            if num in S :
                S.remove(num)
            else :
                S.add(num)


        