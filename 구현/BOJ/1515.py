import sys
input = sys.stdin.readline

# https://hwisaek.tistory.com/entry/Python-sysstdinreadline-%EA%B0%9C%ED%96%89-%EB%AC%B8%EC%9E%90-%EC%B2%98%EB%A6%AC
# readline으로 받을 때 개행문자도 그대로 입력되므로,
# 마지막에 strip() 을 넣어줘야함

nums = input().strip()
# 최솟값 -> 최대한 일의 자리 부터 카운트하는게 이득
ans = 0
tmp = 0

for n in nums :
    num = int(n) + 10 * tmp
    if num > ans :
        ans = num

    else :
        tmp += 1
        next = int(n) + 10 * tmp

        if int(n + "0") < next and int(n + "0") > ans :
            ans = int(n + "0")
        else :
            ans = next

    print(ans)

print(ans)

