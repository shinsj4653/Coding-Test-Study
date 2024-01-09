n = int(input())
p = input()
star_i = p.index('*')

# 접두사, 접미사
# prefix, suffix
# 문자열 -> substr() : 파이썬에선 [:] -> 슬라이싱

pre = p[:star_i]
suf = p[star_i+1:]

for i in range(n) :
    s = input()
    # 반례
    # 패턴 : ab*ab
    # 문자열 : ab
    if len(s) < len(pre) + len(suf):
        print("NE")
    else :
        if pre == s[:len(pre)] and suf == s[len(s) - len(suf):] :
            print("DA")

        else :
            print("NE")
