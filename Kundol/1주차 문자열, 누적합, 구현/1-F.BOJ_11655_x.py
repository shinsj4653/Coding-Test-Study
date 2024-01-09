s = input()
ans = ""

for l in s :
    if l.isalpha() :
        ordNum = ord(l) + 13

        if ord('a') <= ordNum <= ord('z') \
            or ord('A') <= ordNum <= ord('Z') :
            ans += chr(ordNum)

        elif ord('z') < ordNum :
            ans += chr(ordNum - ord('z'))

        elif ord('Z') < ordNum :
            ans += chr(ordNum - ord('Z'))

    else :
        ans += l

print(ans)
