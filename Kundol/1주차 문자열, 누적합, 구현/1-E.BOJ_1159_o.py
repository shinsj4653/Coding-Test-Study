# counting star
# 문자열이니 map
# 하지만, ord 사용하면 숫자로 나타낼 수 있으니 배열사용 가능

# 빈 문자열에 더하는 방식 사용!

n = int(input())
arr = [0] * 26

for i in range(n) :
    arr[ord(input()[0]) - ord('a')] += 1

#print(arr)
s = ""

for i, a in enumerate(arr) :
    if a >= 5 :
        s += chr(ord("a") + i)

print("PREDAJA") if len(s) == 0 else print(s)
