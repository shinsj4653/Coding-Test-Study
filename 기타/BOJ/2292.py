N = int(input())

# 1, 6, 12, 18, 24,
# 1, 7, 19, 37,
num = 1
sum = 1
ans = 1

if N == 1 :
    print(1)
else :
    num += 5
    sum += num
    ans += 1
    while True :
        if N <= sum :
            print(ans)
            break
        else :
            num += 6
            sum += num
            ans += 1

