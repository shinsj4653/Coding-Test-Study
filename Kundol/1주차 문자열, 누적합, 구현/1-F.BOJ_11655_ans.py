# ord('z'), ord('Z) 든, 둘 다 26만큼 빼주면 된다!!
# 차이가 그만큼이니까

s = input()
ans = ""

for l in s :
    # 대문자인경우
    if ord(l) >= 65 and ord(l) < 97 :
        if ord(l) + 13 > 90 :
            ordNum = ord(l) + 13 - 26
        else :
            ordNum = ord(l) + 13

    elif ord(l) >= 97 and ord(l) <= 122 :
        if ord(l) + 13 > 122 :
            ordNum = ord(l) + 13 - 26
        else :
            ordNum = ord(l) + 13

    ans += chr(ordNum)

print(ans)
