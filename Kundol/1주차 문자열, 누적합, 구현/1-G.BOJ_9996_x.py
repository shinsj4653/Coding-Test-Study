# 알파벳 소문자 여러 개, 별표 하나
# 패턴의 첫 부분과 끝 부분만 같으면 됨

# 맞왜틀...

n = int(input())
p = input()
star_i = p.index('*')
# print(star_i)

for i in range(n) :
    s = input()
    print("DA") if s[:star_i] == p[:star_i] and s[len(s) - len(p[star_i + 1:]):] == p[star_i + 1:] else print("NE")

# a*d 1
# abceawfawfedd 13
#
# star_i 3