# 집합에 원소 있는지 여부 파악 : in, not in
# https://www.codingfactory.net/10043

# 문자열에 문자 있는지 여부 파악 : in, not in
# https://asecurity.dev/entry/Python-%ED%8A%B9%EC%A0%95-%EB%AC%B8%EC%9E%90%EC%97%B4str-%ED%8F%AC%ED%95%A8-%EC%9C%A0%EB%AC%B4contains-%ED%99%95%EC%9D%B8-%EB%B0%A9%EB%B2%95
# find의 경우, 그 문자가 문자열에서 시작하는 문자열 인덱스를 반환. 없으면 -1 반환

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
        # https://blockdmask.tistory.com/469
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


        