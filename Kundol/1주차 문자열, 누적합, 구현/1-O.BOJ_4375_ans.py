# 입력을 몇 개 받는지 모르는데, 이는 어떻게 해결?
# -> https://codingwonny.tistory.com/207
# -> try except 구문 활용

# 1 만들기
# -> 전 수에 * 10 + 1
# -> 단, 시간초과 남
# -> mod 법칙 쓰면 됨

# 어차피 i의 배수 찾는 거니까
# -> i의 mod 연산을 절차마다 해줌

import sys
input = sys.stdin.readline

while True :
    try :
        n = int(input())

    except :
        break

    num = 1
    cnt = 1

    while True :
        if num % n != 0 :
            num = num * 10 + 1
            num %= n
            cnt += 1

        else :
            break

    print(cnt)
