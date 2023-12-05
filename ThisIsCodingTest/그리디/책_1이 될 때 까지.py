N, K = map(int, input().split())

result = 0

while N != 1 :
    if N % K == 0 :
        N //= K
    else :
        N -= K

    result += 1

print(result)